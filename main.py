import re
import matplotlib.pyplot as plt

# Define a simple keyboard layout (main keys + numpad + mouse buttons)
keyboard_layout = [
    ['ESC', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BACKSPACE'],
    ['TAB', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    ['CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'ENTER'],
    ['SHIFT', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'SHIFT'],
    ['CTRL', 'WIN', 'ALT', 'SPACE', 'ALT', 'WIN', 'MENU', 'CTRL'],
    ['UP'],
    ['LEFT', 'DOWN', 'RIGHT'],
    ['MOUSE1', 'MOUSE2', 'MOUSE3', 'MOUSE4', 'MOUSE5'],
    ['KP_0', 'KP_1', 'KP_2', 'KP_3', 'KP_4', 'KP_5', 'KP_6', 'KP_7', 'KP_8', 'KP_9', 'KP_PLUS', 'KP_MINUS', 'KP_DEL']
]

# Map config key names to layout names
key_aliases = {
    'mouse1': 'MOUSE1', 'mouse2': 'MOUSE2', 'mouse3': 'MOUSE3', 'mouse4': 'MOUSE4', 'mouse5': 'MOUSE5',
    'space': 'SPACE', 'ctrl': 'CTRL', 'shift': 'SHIFT', 'alt': 'ALT', 'tab': 'TAB', 'capslock': 'CAPS',
    'enter': 'ENTER', 'backspace': 'BACKSPACE', 'uparrow': 'UP', 'downarrow': 'DOWN',
    'leftarrow': 'LEFT', 'rightarrow': 'RIGHT', 'win': 'WIN', 'menu': 'MENU',
    'kp_plus': 'KP_PLUS', 'kp_minus': 'KP_MINUS', 'kp_del': 'KP_DEL',
    'kp_0': 'KP_0', 'kp_1': 'KP_1', 'kp_2': 'KP_2', 'kp_3': 'KP_3', 'kp_4': 'KP_4',
    'kp_5': 'KP_5', 'kp_6': 'KP_6', 'kp_7': 'KP_7', 'kp_8': 'KP_8', 'kp_9': 'KP_9'
}

def normalize_key(key):
    key = key.strip().lower()
    # Try direct alias
    if key in key_aliases:
        return key_aliases[key]
    # Try uppercase (for single letters, numbers, symbols)
    if len(key) == 1:
        return key.upper()
    # Try special cases: e.g. 'capslock' -> 'CAPS', 'uparrow' -> 'UP', etc.
    # Remove common suffixes/prefixes
    if key.endswith('arrow'):
        return key.replace('arrow', '').upper()
    if key.startswith('kp_'):
        return 'KP_' + key[3:]
    # Try matching with layout keys (case-insensitive)
    for row in keyboard_layout:
        for layout_key in row:
            if key == layout_key.lower():
                return layout_key
    return key.upper()

# Parse the config file for binds
binded_keys = set()
with open('autoexec.cfg', encoding='utf-8') as f:
    for line in f:
        m = re.match(r'bind\s+"?([^\s"]+)"?', line.strip(), re.IGNORECASE)
        if m:
            key = normalize_key(m.group(1))
            binded_keys.add(key)

# Visualization
fig, ax = plt.subplots(figsize=(15, 8))
y = 0
for row in keyboard_layout:
    x = 0
    for key in row:
        color = 'lightgreen' if key in binded_keys else 'lightcoral'
        rect = plt.Rectangle((x, -y), 1, 1, facecolor=color, edgecolor='black')
        ax.add_patch(rect)
        ax.text(x+0.5, -y+0.5, key, ha='center', va='center', fontsize=10)
        x += 1.2 if key == 'SPACE' else 1
    y += 1

ax.set_xlim(0, 15)
ax.set_ylim(-len(keyboard_layout), 1)
ax.axis('off')
plt.title('CS2 Key Bindings: Green = Bound, Red = Unbound')
plt.tight_layout()
plt.show()