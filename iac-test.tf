apiVersion: v1
kind: Pod
metadata:
  name: scanner-validation-pod
  labels:
    app: test-fixture
spec:
  containers:
  - name: test-app
    image: nginx:alpine
    securityContext:
      # Scanner should flag this (privileged escalation allowed)
      privileged: true
      allowPrivilegeEscalation: true
      # Scanner should flag this (not explicitly running as a non-root user)
      runAsNonRoot: false
    ports:
    - containerPort: 80
