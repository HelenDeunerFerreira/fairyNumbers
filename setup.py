import cx_Freeze
executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/icone.png")]

cx_Freeze.setup(
    name="Fairy Numbers",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)
