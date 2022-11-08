# Material classes
A python library for common materials in civil and structural engineering. Mostly taken from Norwegian design standards.

## DISCLAIMER:
THIS CAN NOT BE USED AS A SUBSTITUTE FOR ANY TRADITIONAL CAPACITY VERIFICATION IN SERIOUS PROJECTS, AS THERE MAY BE TYPOS OR OUTDATED DATA IN THIS LIBRARY. 

AS ALWAYS IN ENGINEERING, THE ENGINEER IS RESPONSIBLE FOR VERIFYING AND QUALITY CONTROLLING ALL CALCULATIONS.

## Usage

```toml
[tool.poetry.dependencies]
materialclasses={git="https://github.com/egilmonsas/materialclasses.git", branch = "master" }
```

```python
from materialclasses import solidtimber, steel

print(solidtimber.classes.values())
print(steel.classes.values())
```