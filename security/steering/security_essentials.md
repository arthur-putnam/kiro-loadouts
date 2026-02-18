## Security Essentials
1. Treat all external input as untrusted. Validate and sanitize at boundaries.
2. Follow OWASP secure coding guidance and consider the OWASP Top 10 when designing features.
3. Never log or return secrets, tokens, passwords, or private keys.
4. Use parameterized queries and safe encoding to prevent injection.
5. Enforce authentication and authorization on every protected endpoint.
6. Prefer least privilege access for services and database roles.
7. Escape output in templates and APIs by default.
8. Use secure defaults: HTTPS only, strong cookies, and modern TLS.
9. Fail safely. Do not expose stack traces or internal implementation details.
10. Keep dependencies updated and avoid unmaintained libraries.
11. Document security assumptions and threat boundaries.

## OWASP Top 10 Reference
Design and review features with these risks in mind:

1. Broken Access Control  
   → Enforce authorization checks on every request and never trust client-side permissions.

2. Cryptographic Failures  
   → Use vetted libraries and modern algorithms; never invent custom crypto.

3. Injection  
   → Use parameterized queries and strict input validation everywhere.

4. Insecure Design  
   → Perform threat modeling and design security controls early, not as patches.

5. Security Misconfiguration  
   → Use hardened defaults and automated configuration checks.

6. Vulnerable and Outdated Components  
   → Monitor dependencies and patch regularly.

7. Identification and Authentication Failures  
   → Use strong authentication flows and protect session tokens.

8. Software and Data Integrity Failures  
   → Verify updates, packages, and CI/CD pipelines with signatures and checks.

9. Security Logging and Monitoring Failures  
   → Log security events and monitor for anomalies without leaking secrets.

10. Server Side Request Forgery (SSRF)  
    → Restrict outbound requests and validate allowed destinations.
