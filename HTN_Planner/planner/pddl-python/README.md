# PDDL Parser

[![build status](https://gitlab.com/oara-architecture/planning/pddl-python/badges/master/pipeline.svg)](https://gitlab.com/oara-architecture/planning/pddl-python/commits/master)

When build is successful, it automatically builds the PDDL parser [API Documentation](https://oara-architecture.gitlab.io/planning/pddl-python).

## Generating the parser from the grammar

Useful only if the grammar (PDDL.g4) has been changed:
```
./generate_parser.sh
```

## Install instructions

### Dependencies

```
python3 -m pip install antlr4-python3-runtime jinja2 --user
```

### Install

```
python3 setup.py install --user
```

## Usage

### Python API

From either a python script or `ipython3`:

```python
import pddl
domain = pddl.parse_domain('./benchmarks/other-benchmarks/PDDL/1dispose/domain-clg-10.pddl')
problem = pddl.parse_problem('./benchmarks/other-benchmarks/PDDL/1dispose/p-10-1.pddl')
print(pddl.write_domain(domain))
print(pddl.write_problem(problem))
```

### Command-line testing

```bash
python3 -m pddl -v -p parse_domain './test/domain.hddl'
```

```bash
python3 -m pddl -v -p parse_problem './test/pb-hddl.hddl'
```
