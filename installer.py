import subprocess


def main():
    options = {
        "1": ("Update packages", "update_packages.sh"),
        "2": ("Bind keyboard layout to alt+shift", "bind_keyboard_layout.sh"),
        "3": ("Install and configure git", "install_git.sh"),
        "4": ("Install Python", "python_install.sh"),
        "5": ("Create SSH key", "create_ssh_key.sh"),
        "6": ("Install Google Chrome", "install_chrome.sh"),
        "7": ("Install PyCharm", "install_pycharm.sh"),
        "8": ("Install VS Code", "install_vscode.sh"),
        "9": ("Install Vim", "install_vim.sh"),
        "10": ("Install Docker", "install_docker.sh"),
        "11": ("Install Docker Compose", "install_docker_compose.sh"),
        "12": ("Install PostgreSQL", "install_postgresql.sh"),
        "13": ("Install GCC", "gcc.sh"),
        "14": ("Install OBS", "obs.sh"),
        "15": ("Install NVIDIA drivers", "nvidia_drivers.sh"),
        "16": ("Install Spotify", "install_spotify.sh"),
    }

    while True:
        print("\nPlease choose what you want to install:")

        for key, value in options.items():
            print(f"{key}. {value[0]}")

        choice = input("Enter your choice (or 'E' to exit): ").strip()

        if choice.lower() == "e":
            print("Exiting...")
            break

        if choice in options:
            script_name = options[choice][1]
            subprocess.run(["bash", script_name])
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
