#!/bin/bash

AGENT_FILES=("student_agents/simple_reflex_agent.py" "student_agents/random_agent.py")

for s in 2 4 8 16 32 64 128; do
    for dr in 0.1 0.2 0.4 0.8; do
        for i in {1..10}; do
            for AGENT_FILE in "${AGENT_FILES[@]}"; do
                python3 run_agent.py --agent-file "$AGENT_FILE" --size "$s" --dirt-rate "$dr" --record
            done
        done
    done
done