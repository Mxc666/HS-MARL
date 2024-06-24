# OS: Linux

# Package

1. numpy - 1.20.3

2. antlr4-python3-runtime - 4.7

3. gym - 0.21.0

4. networkx - 2.6.3

5. pandas - 1.3.5

6. pillow - 8.4.0

7. python - 3.7.3

8. pytorch - 1.7.1

9. wandb - 0.12.21

10. jinja2 - 3.1.2

11. colorlog - 6.6.0

12. pydot - 1.4.2

13. sortedcontainers - 2.4.0


# Compile HTN Planner - pyHIPOP

cd HTN_Planner/planner/pddl-python

python3 setup.py install

cd ../..

python3 setup.py install

# Run

**NOTE** 
1. Please put the *code* folder in the *root* directory

2. If you want to plot the learning curve, you need to assign the *user_name* variable with the specific *user's name* in the argParser file.

3. Or set the *use_wandb* variable in the argParser file to *False*, in which case the user's name does not have to be provided, and the learning curve will not be output.

## FindTreasure

### SOMARL

1. **seed - 1**: run main_FindTreasure_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_FindTreasure_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_FindTreasure_SOMAPPO_Seed_100.py


## GoTogether

### SOMARL

1. **seed - 1**: run main_GoTogether_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_GoTogether_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_GoTogether_SOMAPPO_Seed_100.py


## MoveBox-raw

### SOMARL

1. **seed - 1**: run main_MoveBox_task0_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_MoveBox_task0_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_MoveBox_task0_SOMAPPO_Seed_100.py

## MoveBox-task1

### SOMARL

1. **seed - 1**: run main_MoveBox_task1_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_MoveBox_task1_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_MoveBox_task1_SOMAPPO_Seed_100.py

## MoveBox-task2

### SOMARL

1. **seed - 1**: run main_MoveBox_task2_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_MoveBox_task2_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_MoveBox_task2_SOMAPPO_Seed_100.py

## MoveBox-task3

### SOMARL

1. **seed - 1**: run main_MoveBox_task3_SOMAPPO_Seed_1.py

2. **seed - 75**: run main_MoveBox_task3_SOMAPPO_Seed_75.py

3. **seed - 100**: run main_MoveBox_task3_SOMAPPO_Seed_100.py

