import cx_Freeze

executables = [cx_Freeze.Executable("race_it.py")]
cx_Freeze.setup(
            name="RACEY",
            version = "1.1",
            options={"build_exe":{"packages":["pygame"],
                                  "include_files":["car1.png","Crash.wav","Burnt.wav"]}},
            executables = executables)
