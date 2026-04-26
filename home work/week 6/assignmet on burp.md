# Burp Suite and cURL Tasks: Theoretical Answers

## 1. Repeater Manipulation Task

### Adding a new parameter and sending it
When a new parameter is added to a request, the server processes that parameter according to its application logic. If the parameter is unexpected or not implemented, the server may ignore it and return the same response. If the parameter corresponds to a valid server-side variable, the response may change to reflect the new input, potentially triggering different application states, error messages, or data outputs.

### Modifying User-Agent header
Changing the User-Agent header can cause the server to return different content optimized for specific browsers or devices. Some applications serve mobile versions, different JavaScript bundles, or alternate CSS frameworks based on User-Agent detection. Security mechanisms may also block or allow requests based on known bot signatures in the User-Agent string. A changed User-Agent may bypass client-side restrictions or trigger server-side rendering differences.

### Adding X-Test: hello header
Adding a custom header like X-Test typically results in the server either ignoring the header completely or, if the application is designed to recognize custom headers, logging the value or using it for debugging purposes. Some security tools and WAFs may flag or block requests containing unexpected custom headers. In most default configurations, adding X-Test produces no visible change in the response body unless the application specifically checks for it.

### Modifying Cookie value
Changing the Cookie value directly affects session management and authentication state. An invalid or expired cookie typically results in a redirect to a login page, a 401 Unauthorized status code, or an error message indicating session failure. A valid cookie for a different user (if guessed or stolen) returns that user's data, representing an Insecure Direct Object Reference vulnerability. Modifying cookie attributes may also change user role permissions or access to specific application features.

### Changing HTTP method from GET to POST
Changing GET to POST alters how parameters are transmitted. In a GET request, parameters appear in the URL query string. In a POST request, parameters are sent in the message body. Servers expecting parameters in the body will return an error, often 405 Method Not Allowed, when receiving GET requests. Conversely, servers that accept both methods may process the request identically or apply different validation rules per method. The response may change from successful data retrieval to an error, or from a form display to a submission confirmation.

### Response change summary by modification type

| Modification | Expected Response Change |
|--------------|-------------------------|
| New parameter | Generally ignored; no change unless parameter is valid server-side variable |
| User-Agent change | Different content optimization; possible security block |
| X-Test header | Typically ignored; no visible change |
| Cookie modification | Session invalidation; redirect to login; possible privilege change |
| GET to POST | Method not allowed error; parameter parsing difference; possible success if dual-method endpoint |

---

## 2. Intruder Practical Task

### Setup process
The login or input request is captured in Burp Proxy when the user submits credentials. The request is then right-clicked and sent to Intruder using the "Send to Intruder" context menu option. In the Positions tab, payload positions are cleared by clicking "Clear §" and then the username parameter value is highlighted and the "Add §" button is clicked to mark it as a payload position.

### Payload configuration
The payload set is configured with three test values: admin, test, and 123. These are entered manually in the Payload Options section. The attack type is typically left as Sniper, which iterates through each payload value one at a time while leaving other positions unchanged.
### Observable response differences
When the attack is started, the Intruder results table displays each request with columns for status code, response length, and response time. A value that behaves differently from others is identified by examining these columns for anomalies.

A request that returns a different status code, such as 200 instead of 401, or 302 redirect to a dashboard instead of a login page, indicates a successful authentication bypass. A significantly different response length suggests different content is being returned, such as an error message versus a welcome page. Different response times may indicate server-side processing differences, such as database lookups versus immediate rejection.

### Identifying anomalous input
The input that behaves differently is the one where the server returns a successful authentication response rather than a failure message. For example, if admin returns a 302 redirect to /dashboard while test and 123 return 401 Unauthorized, admin is the valid credential. The user can then examine the response content of the successful request to confirm access or extract additional information such as session tokens or user profile data.

---

## 3. Proxy + cURL Task

### Sending a request through proxy to Burp Suite
To send a request through a proxy to Burp Suite, the cURL command includes the --proxy flag with the Burp Suite listening address and port. The command syntax is:

curl --proxy http://127.0.0.1:8080 http://target.com/page

For HTTPS requests through the proxy, the -k flag is often added to ignore certificate validation errors because Burp Suite presents its own certificate:

curl --proxy http://127.0.0.1:8080 -k https://target.com/page

### What happens to the request inside Burp Suite
When the request passes through Burp Suite, the following occurs sequentially:

The request is intercepted if the Intercept button is set to "on". The user can review, modify, or drop the request before forwarding. The request is logged in the HTTP History tab regardless of intercept status. Burp Suite records the full request including method, URL, headers, body, and source IP address. The response is also captured as it returns through the proxy. Burp Suite may apply any active extensions or scanner checks to the traffic. The request is then forwarded to the target server unmodified unless the user made changes during interception. The response is similarly captured before being returned to cURL.

---

## 4. Request Replay with cURL

### Capturing a request in Burp Proxy
While browsing the target application with Burp Proxy enabled, the user navigates to the desired page or submits a form. The request appears in the HTTP History tab. The user selects the request and copies it as a cURL command by right-clicking and selecting "Copy as curl command".

### Replaying with cURL
The copied command is pasted into a terminal and executed. The command contains all headers, cookies, and parameters exactly as captured. The response is displayed in the terminal output.

### Modifying a parameter and resending
To modify a parameter, the user edits the cURL command before execution. For a GET request, the parameter value is changed directly in the URL query string. For a POST request, the -d parameter value is modified. The edited command is then executed. The modified request may produce a different response based on the changed parameter value. For example, changing an ID parameter from 1 to 2 may return data for a different resource, revealing potential authorization vulnerabilities.

---

## 5. cURL Flags Explanation

### -X flag
The -X flag specifies the HTTP method to use for the request. The default method is GET if no -X flag is provided. Common values include GET, POST, PUT, DELETE, PATCH, and HEAD. Example: -X POST changes the request method to POST.
### -H flag
The -H flag adds or modifies an HTTP header in the request. Multiple -H flags can be used for multiple headers. The header is provided as a string in "Header-Name: value" format. Example: -H "User-Agent: CustomBot" replaces the default User-Agent. The -H flag is also used for authentication tokens: -H "Authorization: Bearer token123".

### -d flag
The -d flag sends data in the request body, typically for POST requests. When -d is used, cURL automatically changes the request method to POST unless -X specifies otherwise. The data can be URL-encoded key-value pairs or raw JSON. Example: -d "username=admin&password=pass" sends form data. For JSON data, the Content-Type header must also be set: -H "Content-Type: application/json" -d '{"key":"value"}'.

### -i flag
The -i flag includes the HTTP response headers in the output along with the response body. Without -i, cURL displays only the response body. The -i flag is essential for debugging because it shows status codes, server headers, Set-Cookie directives, and Content-Type information. Example output includes HTTP/1.1 200 OK followed by all headers, a blank line, then the response body.

### -L flag
The -L flag instructs cURL to follow HTTP redirects automatically. When a server responds with a 301, 302, 303, 307, or 308 status code and a Location header, cURL resends the request to the new URL. Without -L, cURL displays the redirect response without following it. The -L flag is critical for testing login flows and applications that redirect after form submission.

### --proxy flag
The --proxy flag routes the request through a specified proxy server. The syntax is --proxy protocol://host:port. Example: --proxy http://127.0.0.1:8080 routes traffic through Burp Suite. The --proxy flag is used for intercepting traffic, debugging requests, bypassing network restrictions, and analyzing application behavior in a controlled environment.

### cURL with Burp Suite in web testing workflows

cURL integrated with Burp Suite supports the following workflows:

Request generation: Requests captured in Burp are exported as cURL commands for scripting and automation reproduction.

Parameter fuzzing: cURL commands are modified with different parameter values and executed in loops to test for injection vulnerabilities.

Header manipulation: Custom headers are added or modified using -H flags to test security controls and server behavior.

Proxy debugging: The --proxy flag routes cURL traffic through Burp, allowing real-time inspection and modification of automated tool requests.

Regression testing: Captured cURL commands are saved as test scripts to verify that vulnerabilities are patched or that application behavior remains consistent after updates.

Authentication replay: Session cookies extracted from Burp are used in cURL commands with -H "Cookie: ..." to test authenticated endpoints without using a browser.

The combination of Burp Suite for interactive exploration and cURL for scripted testing provides complete coverage for manual and automated web security testing workflows.
