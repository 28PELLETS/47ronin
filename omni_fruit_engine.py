import os
from blueprint_corrector import BluePrintCorrector
from Willow_BSI_Core import WillowBSI

class FruitEngine:
    def __init__(self):
        self.moderator = BluePrintCorrector()
        self.gardener = WillowBSI()
        print("[FRUIT] Engine primed. Ready for final fabrication.")

    def serve_truth(self, raw_swarm_data):
        """The hand-off. Delivering the final product."""
        print("[FRUIT] Receiving output from the 47 Ronin...")
        
        # 1. Calibrate through the Moderator (Dad's Logic)
        refined_truth = self.moderator.calibrate(raw_swarm_data)
        
        # 2. Final Clean (The Dishwasher/Gardener)
        self.gardener.gardener_prune()
        
        # 3. The Fruit
        print(f"\n--- FINAL MISSION CONTROL TRUTH ---")
        print(f"RESULT: {refined_truth.upper()}")
        print(f"--- 0.01% Handshake Complete ---\n")
        
        return refined_truth

if __name__ == "__main__":
    engine = FruitEngine()
    engine.serve_truth("The omni will now fabricate the final language layer.")
