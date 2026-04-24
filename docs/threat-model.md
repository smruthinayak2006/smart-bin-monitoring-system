# Threat Model

## Threats

1 Sensor spoofing
Attacker sends fake low fill values.

Mitigation:
- Range validation
- Sensor sanity checks

---

2 MQTT tampering
Fake messages injected.

Mitigation:
- Authenticated MQTT
- TLS encryption

---

3 Device cloning
Rogue node impersonates bin.

Mitigation:
- Unique device IDs
- Signed telemetry