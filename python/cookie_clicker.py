import tkinter as tk

cookies = 0
cookies_per_click = 1
cookies_per_second = 0
player_name = "Baker"

BG = "#f7e7ce"
BUTTON_BG = "#d69b52"
BUTTON_ACTIVE = "#edbd78"

# Collection: stores the upgrades used by the shop and purchase logic.
shop_items = [
    {
        "id": "better_dough",
        "name": "Better Dough",
        "description": "+1 cookie per click",
        "cost": 10,
        "effect": "click",
        "amount": 1,
        "owned": 0,
    },
    {
        "id": "rolling_pin",
        "name": "Rolling Pin",
        "description": "+5 cookies per click",
        "cost": 75,
        "effect": "click",
        "amount": 5,
        "owned": 0,
    },
    {
        "id": "golden_spatula",
        "name": "Golden Spatula",
        "description": "+20 cookies per click",
        "cost": 300,
        "effect": "click",
        "amount": 20,
        "owned": 0,
    },
    {
        "id": "auto_clicker",
        "name": "Auto Clicker",
        "description": "+1 cookie per second",
        "cost": 50,
        "effect": "automatic",
        "amount": 1,
        "owned": 0,
    },
    {
        "id": "grandma",
        "name": "Grandma",
        "description": "+5 cookies per second",
        "cost": 200,
        "effect": "automatic",
        "amount": 5,
        "owned": 0,
    },
    {
        "id": "cookie_factory",
        "name": "Cookie Factory",
        "description": "+25 cookies per second",
        "cost": 1000,
        "effect": "automatic",
        "amount": 25,
        "owned": 0,
    },
]

shop_buttons = {}


def update_display(message=None):
    # Output: updates the game totals, shop prices, and status message.
    cookie_label.config(text=f"{player_name}'s cookies: {cookies}")
    power_label.config(text=f"Cookies per click: {cookies_per_click}")
    auto_label.config(text=f"Cookies per second: {cookies_per_second}")

    for item in shop_items:
        shop_buttons[item["id"]].config(
            text=f"Buy — {item['cost']} cookies | Owned: {item['owned']}"
        )

    if message is not None:
        status_label.config(text=message)


def set_player_name():
    global player_name

    # Input: reads the player's name from the entry box.
    entered_name = name_entry.get().strip()

    if entered_name:
        player_name = entered_name
        update_display(f"Welcome, {player_name}!")
    else:
        update_display("Please enter a name.")


def click_cookie():
    global cookies

    cookies += cookies_per_click
    update_display("Keep baking!")


# Parameter: item_id determines which upgrade to purchase.
def buy_item(item_id):
    global cookies, cookies_per_click, cookies_per_second

    # Iteration: searches the core shop collection.
    for item in shop_items:
        # Selection: checks the chosen item and available cookies.
        if item["id"] == item_id:
            if cookies < item["cost"]:
                update_display(
                    f"You need {item['cost'] - cookies} more cookies!"
                )
                return

            # Sequencing: pay, update ownership, apply effect,
            # increase the price, and display the result.
            cookies -= item["cost"]
            item["owned"] += 1

            if item["effect"] == "click":
                cookies_per_click += item["amount"]
            elif item["effect"] == "automatic":
                cookies_per_second += item["amount"]

            item["cost"] += max(1, item["cost"] // 2)
            update_display(f"Purchased: {item['name']}!")
            return

    update_display("That upgrade does not exist.")


def show_page(page):
    page.tkraise()


def auto_click():
    global cookies

    cookies += cookies_per_second
    update_display()
    root.after(1000, auto_click)


root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("800x850")
root.resizable(False, False)
root.configure(bg=BG)

title_label = tk.Label(
    root,
    text="COOKIE CLICKER",
    font=("Arial", 24, "bold"),
    bg=BG,
)
title_label.pack(pady=(15, 10))

name_frame = tk.Frame(root, bg=BG)
name_frame.pack(pady=5)

tk.Label(
    name_frame,
    text="Enter your name:",
    font=("Arial", 11),
    bg=BG,
).pack(side=tk.LEFT, padx=5)

name_entry = tk.Entry(
    name_frame,
    font=("Arial", 11),
    width=18,
)
name_entry.pack(side=tk.LEFT, padx=5)

tk.Button(
    name_frame,
    text="Set Name",
    command=set_player_name,
    bg=BUTTON_BG,
    activebackground=BUTTON_ACTIVE,
).pack(side=tk.LEFT, padx=5)

cookie_label = tk.Label(
    root,
    font=("Arial", 20),
    bg=BG,
)
cookie_label.pack(pady=(12, 5))

power_label = tk.Label(
    root,
    font=("Arial", 12),
    bg=BG,
)
power_label.pack(pady=2)

auto_label = tk.Label(
    root,
    font=("Arial", 12),
    bg=BG,
)
auto_label.pack(pady=2)

navigation = tk.Frame(root, bg=BG)
navigation.pack(pady=12)

page_container = tk.Frame(root, bg=BG)
page_container.pack(fill=tk.BOTH, expand=True, padx=20)

page_container.grid_rowconfigure(0, weight=1)
page_container.grid_columnconfigure(0, weight=1)

game_page = tk.Frame(page_container, bg=BG)
upgrade_page = tk.Frame(page_container, bg=BG)

for page in (game_page, upgrade_page):
    page.grid(row=0, column=0, sticky="nsew")

tk.Button(
    navigation,
    text="Bake Cookies",
    command=lambda: show_page(game_page),
    font=("Arial", 12),
    bg=BUTTON_BG,
    activebackground=BUTTON_ACTIVE,
    width=18,
).pack(side=tk.LEFT, padx=5)

tk.Button(
    navigation,
    text="Upgrade Menu",
    command=lambda: show_page(upgrade_page),
    font=("Arial", 12),
    bg=BUTTON_BG,
    activebackground=BUTTON_ACTIVE,
    width=18,
).pack(side=tk.LEFT, padx=5)

tk.Label(
    game_page,
    text="Time to bake!",
    font=("Arial", 20, "bold"),
    bg=BG,
).pack(pady=(50, 20))

tk.Button(
    game_page,
    text="CLICK ME!",
    font=("Arial", 28, "bold"),
    command=click_cookie,
    bg=BUTTON_BG,
    activebackground=BUTTON_ACTIVE,
    width=14,
    height=3,
).pack(pady=20)

tk.Label(
    game_page,
    text="Visit the Upgrade Menu to boost your bakery.",
    font=("Arial", 12),
    bg=BG,
).pack(pady=15)

tk.Label(
    upgrade_page,
    text="UPGRADE SHOP",
    font=("Arial", 18, "bold"),
    bg=BG,
).pack(pady=(5, 10))

for item in shop_items:
    item_frame = tk.Frame(
        upgrade_page,
        bg=BG,
        highlightbackground=BUTTON_BG,
        highlightthickness=1,
    )
    item_frame.pack(fill=tk.X, pady=4, padx=10)

    details_frame = tk.Frame(item_frame, bg=BG)
    details_frame.pack(side=tk.LEFT, padx=10, pady=8)

    tk.Label(
        details_frame,
        text=item["name"],
        font=("Arial", 12, "bold"),
        bg=BG,
        anchor="w",
    ).pack(anchor="w")

    tk.Label(
        details_frame,
        text=item["description"],
        font=("Arial", 10),
        bg=BG,
        anchor="w",
    ).pack(anchor="w")

    buy_button = tk.Button(
        item_frame,
        font=("Arial", 10),
        # Function call: purchases the upgrade linked to this button.
        command=lambda item_id=item["id"]: buy_item(item_id),
        bg=BUTTON_BG,
        activebackground=BUTTON_ACTIVE,
        width=32,
    )
    buy_button.pack(side=tk.RIGHT, padx=10, pady=8)
    shop_buttons[item["id"]] = buy_button

status_label = tk.Label(
    root,
    text="Keep baking!",
    font=("Arial", 12),
    bg=BG,
    wraplength=750,
)
status_label.pack(pady=15)

show_page(game_page)
update_display()
root.after(1000, auto_click)
root.mainloop()
