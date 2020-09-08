import os
import sys
from shutil import copyfile
import utils.mdi_mech_tests as mtests
import utils.check_mdi_nodes as na

# Path to this file
file_path = os.path.dirname(os.path.realpath(__file__))

# Path to the top-level directory
base_path = os.path.dirname( os.path.dirname( file_path ) )



# Generate the report
############
# REPLACE WITH MODULE
############
os.chdir( str(base_path) )
os.system("python ./MDI_Mechanic/scripts/utils/reset_report.py")


def generate_report():
    # Verify that the engine has been built / installed correctly
    try:
        mtests.test_validate()
        print("Success: Able to verify that the engine was built")
        src_location = os.path.join(base_path, "report", "badges", "-working-success.svg")
        dst_location = os.path.join(base_path, "report", "dynamic_badges", "step_engine_build.svg")
        copyfile(src_location, dst_location)
    except:
        raise Exception("Error: Unable to verify that the engine was built.")

    # Verify that the engine test calculation can be run
    try:
        mtests.test_engine()
        print("Success: Engine test(s) succeeded.")
        src_location = os.path.join(base_path, "report", "badges", "-working-success.svg")
        dst_location = os.path.join(base_path, "report", "dynamic_badges", "step_engine_test.svg")
        copyfile(src_location, dst_location)
    except:
        raise Exception("Error: Engine test(s) failed.")

    # Verify that the engine test calculation can be run
    try:
        mtests.test_min()
        print("Success: Engine passed minimal MDI functionality test.")
        src_location = os.path.join(base_path, "report", "badges", "-working-success.svg")
        dst_location = os.path.join(base_path, "report", "dynamic_badges", "step_min_engine.svg")
        copyfile(src_location, dst_location)

        ############
        # TEMPORARY
        os.chdir( str(base_path) )
        ############
    except:
        raise Exception("Error: Engine failed minimal MDI functionality test.")

    # Check if the engine correctly errors upon receiving an unsupported command
    try:
        mtests.test_unsupported()
        print("Success: Engine errors out upon receiving an unsupported command.")
        src_location = os.path.join(base_path, "report", "badges", "-working-success.svg")
        dst_location = os.path.join(base_path, "report", "dynamic_badges", "step_unsupported.svg")
        copyfile(src_location, dst_location)

        ############
        # TEMPORARY
        os.chdir( str(base_path) )
        ############
    except:
        raise Exception("Error: Engine does not error out upon receiving an unsupported command.")

    # Perform the node analysis
    try:
        na.analyze_nodes()
        print("Success: Detected MDI nodes.")

        # Copy the success badge for this step
        src_location = os.path.join(base_path, "report", "badges", "-working-success.svg")
        dst_location = os.path.join(base_path, "report", "dynamic_badges", "step_mdi_nodes.svg")
        copyfile(src_location, dst_location)

        # Prepend the Travis badge to README.md
        readme_path = os.path.join(base_path, "MDI_Mechanic", ".temp", "README.temp")
        badge_path = os.path.join(base_path, ".travis", "travis_badge.md")
        badge = None
        readme = None
        with open(badge_path, 'r') as original: badge = original.read()
        with open(readme_path, 'r') as original: readme = original.read()
        with open(readme_path, 'w') as modified: modified.write(badge + readme)
    
        # Copy README.temp over README.md
        src_location = os.path.join(base_path, "MDI_Mechanic", ".temp", "README.temp")
        dst_location = os.path.join(base_path, "README.md")
        copyfile(src_location, dst_location)
    except:
        raise Exception("Error: Unable to detect MDI nodes.")

# Generate the report
generate_report()
