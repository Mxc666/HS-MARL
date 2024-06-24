#!/bin/bash
java -cp "./libs/antlr-4.8-complete.jar:$CLASSPATH" org.antlr.v4.Tool -Dlanguage=Python2 -listener -visitor -o pddl/parser PDDL.g4
