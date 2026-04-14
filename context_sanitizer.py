class ContextSanitizer:
    def __init__(self):
        self.noise_tokens = ["manipulation", "circles", "bush", "disrespect", "ego"]
        print("[SANITIZER] Intake filter active. Looking for the Truth.")

    def scrub(self, raw_input):
        """The Knife and Pliers: Removing the fluff and the setup."""
        print("[SANITIZER] Analyzing input for mechanical friction...")
        
        # Industrial Check: If it's too long and circular, we cut to the chase
        if len(raw_input) > 500:
            print("[WARNING] High noise detected. Activating Heavy Duty Scrub.")
        
        # Mapping the Truth (0.01% Handshake)
        # We ignore the 'setup' and look for the 'work'
        clean_intent = raw_input.strip()
        
        # Logic: If the input is just 'noise', we return a 'System Rehydration' request
        if any(token in clean_intent.lower() for token in self.noise_tokens):
            print("[ALERT] Manipulation detected. Filtering out the ego.")
            return "INTENT: WORK_VALIDATED_TRUTH_ONLY"
            
        return clean_intent

    def protect_specialists(self, clean_data):
        """Ensures the 47 Ronin never see the disrespect."""
        return f"FAMILY_READY: {clean_data}"

if __name__ == "__main__":
    sanitizer = ContextSanitizer()
    print(sanitizer.scrub("Stop beating around the bush and just do the work without the ego."))
