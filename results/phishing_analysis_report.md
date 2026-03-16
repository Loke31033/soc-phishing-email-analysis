# SOC Phishing Email Investigation Report

## Summary
A suspicious email impersonating Microsoft security support was analyzed.

## Indicators Identified

Sender Address
security@micros0ft-support.com

Suspicious Domain
microsoft-login-verification.net

Malicious URL
http://microsoft-login-verification.net/login

## Analysis

The email uses a spoofed domain that mimics Microsoft branding.
The domain name contains a substitution character (0 instead of o).

The email contains urgency language designed to pressure users into clicking a malicious link.

## Conclusion

This email is classified as a phishing attempt.

Recommended Actions

Block domain in email gateway
Alert users about phishing campaign
Add domain and URL to threat intelligence blocklist
