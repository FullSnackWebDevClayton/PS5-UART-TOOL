from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": [
        "os",
        "certifi",
        "charset_normalizer",
        "idna",
        "PIL",
        "serial",
        "requests",
        "six",
        "urllib3",
        "wx",
    ], "excludes": []}

# Call setup function
setup(
    name="PS5 UART Tool",
    version="0.1",
    description="PS5 UART Tool by Tech Centre UK",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base="gui", icon="windows.ico", target_name="PS5 UART Tool")]
)


# To build the windows executable, run the following command in the terminal:
# python windows-setup.py bdist_msi
