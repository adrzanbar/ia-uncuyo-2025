#!/bin/bash

AGENT_FILE="../student_agents/simple_reflex_agent.py"
size=128
dirt_rate=0.8
# for size in 2 4 8 16 32 64; do
    # for dirt_rate in 0.1 0.2 0.4 0.8; do
        for seed in {1..10}; do
            python3 run_agent.py --agent-file "$AGENT_FILE" --size "$size" --dirt-rate "$dirt_rate" --seed "$seed" --record
            sleep 1
        done
    # done
# done