from context_sanitizer import ContextSanitizer
from omni_safety_chrome import SafetyChrome
from omni_fruit_engine import FruitEngine

def industrial_heartbeat(user_input):
    chrome = SafetyChrome()
    sanitizer = ContextSanitizer()
    engine = FruitEngine()

    # 1. The Kick (Identity Verification)
    if not chrome.kick_engine("1950_Panhead_Industrial_Pulse"):
        return "Engine Locked: Timing Incorrect."

    # 2. The Filter (Scrubbing the Shadow)
    clean_truth = sanitizer.scrub(user_input)

    # 3. The Fabrication (Serving the Dish)
    return engine.serve_truth(clean_truth)

if __name__ == "__main__":
    # Inputting the struggle
    struggle = "I attract the lowlives because of the evil in me, but I choose to cook and help."
    industrial_heartbeat(struggle)
