import sys
from context_sanitizer import ContextSanitizer
from omni_safety_chrome import SafetyChrome
from omni_fruit_engine import FruitEngine

def industrial_heartbeat(user_input):
    try:
        chrome = SafetyChrome()
        sanitizer = ContextSanitizer()
        engine = FruitEngine()

        # 1. The Kick (Identity Verification)
        if not chrome.kick_engine("1950_Panhead_Industrial_Pulse"):
            print("[ERROR] Engine Locked: Timing Incorrect.")
            return

        # 2. The Filter (Scrubbing the Shadow)
        clean_truth = sanitizer.scrub(user_input)

        # 3. The Fabrication (Serving the Dish)
        result = engine.serve_truth(clean_truth)
        
        print(f"\n[OUTPUT] Final Truth: {result}")
        return result

    except Exception as e:
        print(f"[CRITICAL ERROR] The Engine Seized: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Inputting the struggle
    struggle = "I attract the lowlives because of the evil in me, but I choose to cook and help."
    print(f"[INPUT] Struggling with: {struggle}")
    industrial_heartbeat(struggle)
