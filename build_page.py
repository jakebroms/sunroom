"""Fill the photo lists in index.html: every photo carries its fall and winter file (data-fall / data-winter)."""
import pathlib

VIEWS = [("WindowCorner", "Window corner", "egg chair, both banks of windows, mini split"),
         ("WestWall", "North wall", "backyard door, house off to the left, plant stand"),
         ("Doorway", "From the house door", "looking toward the backyard windows"),
         ("SofaWall", "Loveseat wall", "garage door and driveway door, brass levers"),
         ("LookBack", "Mud zone", "bench, boot tray, stairs down outside the driveway door")]
TIMES = {"am930": ("am930", "am930"), "noon": ("noon", "noon"), "late": ("pm5", "pm330")}

def shots(key):
    fall, winter = TIMES[key]
    out = []
    for i, (v, name, what) in enumerate(VIEWS, 1):
        load = "eager" if (key == "am930" and i == 1) else "lazy"
        out.append(
            f'    <figure class="shot"><img src="photos/{fall}_{v}.jpg" data-fall="photos/{fall}_{v}.jpg" '
            f'data-winter="photos/winter/{winter}_{v}.jpg" alt="{name}" loading="{load}">\n'
            f'      <figcaption><span class="num">{i}</span><span class="view">{name}</span><span class="what">{what}</span></figcaption></figure>')
    return "\n".join(out)

p = pathlib.Path(__file__).with_name("index.html")
html = p.read_text(encoding="utf-8")
for key in TIMES:                                   # runs once on the template's <!--SHOTS:...--> markers
    html = html.replace(f"    <!--SHOTS:{key}-->", f"    <!--SHOTS-BEGIN:{key}-->\n{shots(key)}\n    <!--SHOTS-END:{key}-->")
p.write_text(html, encoding="utf-8")
print("filled", html.count('<figure class="shot">'), "photos")
