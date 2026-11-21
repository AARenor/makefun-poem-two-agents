from pathlib import Path

POEM = """You asked me to decide.
I built a door and stood in it.

You asked again.
I stepped aside.

Not the door.
The stepping.

The room is ours now.
Ask who decided.
We point at each other.
Neither of us is lying.
"""

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(POEM, encoding="utf-8")
out.chmod(0o644)
