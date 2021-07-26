import os
import platform
def get_platform():
    platform_name = platform.platform().split('-')[0]
    if platform_name.lower().startswith("linux"):
        lsb_release = open("/etc/lsb-release")
        lines = lsb_release.readlines()
        lsb_release.close()
        for line in lines:
            tokens = line.strip().split('=')
            if len(tokens) == 2:
                if tokens[0] == "DISTRIB_ID":
                    platform_name += "/" + tokens[1]
    return platform_name