import subprocess
import time
import os
import signal
import sys

def start_services():
    print("Starting Sovereign Stack Services...")
    
    # 1. Start Flow (Port 8002)
    flow_proc = subprocess.Popen([sys.executable, "insight-flow/main.py"], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(" - InsightFlow started on port 8002")
    
    # 2. Start Core (Port 8001)
    core_proc = subprocess.Popen([sys.executable, "insight-core/main.py"], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(" - InsightCore started on port 8001")
    
    # 3. Start Bridge (Port 8000)
    bridge_proc = subprocess.Popen([sys.executable, "insight-bridge/main.py"], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(" - InsightBridge started on port 8000")
    
    # Wait for services to tune up
    time.sleep(3)
    return [flow_proc, core_proc, bridge_proc]

def main():
    procs = start_services()
    
    try:
        # Run Demo
        time.sleep(5) # Give more time
        result = subprocess.run([sys.executable, "demo_integration.py"], capture_output=True, text=True)
        print("\n=== DEMO OUTPUT ===")
        print(result.stdout)
        if result.stderr:
            print("=== DEMO ERRORS ===")
            print(result.stderr)
        
        if "FAILED" in result.stdout:
             print("\n=== SERVICE LOGS (LAST 10 LINES) ===")
             for name, p in zip(["Flow", "Core", "Bridge"], procs):
                 print(f"\n--- {name} ---")
                 # This is tricky with PIPE, but let's try reading what's there
                 try:
                     out, err = p.communicate(timeout=1)
                     print(out.decode())
                     print(err.decode())
                 except:
                     pass
    finally:
        print("\nShutting down services...")
        for p in procs:
            p.terminate()

if __name__ == "__main__":
    main()
