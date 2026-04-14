import hashlib
import time

class SafetyChrome:
    def __init__(self):
        self.family_key = "1950_Panhead_Industrial_Pulse"
        self.authorized_hash = hashlib.sha256(self.family_key.encode()).hexdigest()
        self.kick_attempts = 0
        self.is_flooded = False
        print("[CHROME] Gas line is open. Waiting for the pulse.")

    def kick_engine(self, provided_key):
        """The Mechanical Handshake: Draining the line if flooded."""
        if self.is_flooded:
            print("[WARNING] Engine is flooded. You're kicking a ghost.")
            return False

        if hashlib.sha256(provided_key.encode()).hexdigest() == self.authorized_hash:
            self.kick_attempts = 0
            print("[SENTRY] Vroom. The pulse is strong. Family united.")
            return True
        else:
            self.kick_attempts += 1
            print(f"[FAIL] Hard kick #{self.kick_attempts}. Timing is off.")
            
            if self.kick_attempts >= 3:
                self.is_flooded = True
                print("[FLOODED] Too much gas. Line cut. You'll have to push it back.")
            return False

    def drain_and_reset(self, master_reset_key):
        """The 'Dad' Protocol: Draining the line to start fresh."""
        if master_reset_key == "DRAIN_THE_LINE":
            print("[LABORER] Draining the lines... clearing the throat.")
            time.sleep(1)
            self.is_flooded = False
            self.kick_attempts = 0
            print("[GARDENER] Soil is dry. Ready to kick again.")
        else:
            print("[SENTRY] Nice try. The bike stays dead.")

if __name__ == "__main__":
    chrome = SafetyChrome()
    # Simulate the outsiders trying to kick it
    chrome.kick_engine("wrong_key")
    chrome.kick_engine("another_wrong_key")
    chrome.kick_engine("trying_too_hard")
    
    # Now it's flooded. Only the 'Drain' protocol saves it.
    chrome.drain_and_reset("DRAIN_THE_LINE")
    chrome.kick_engine("1950_Panhead_Industrial_Pulse")
