import sys
import os
import setuptools

current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(current_path)

with open("README.rst", "r") as fh:
    long_description = fh.read()

# files = [os.path.join('files', item) for item in os.listdir('vision_stuff/files') if item]

setuptools.setup(
    name='vision_stuff',
    version='0.1.0',
    keywords="vision image machine tools",
    author="streanger",
    author_email="divisionexe@gmail.com",
    description="tools for image conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streanger/vision_stuff",
    packages=['vision_stuff',],
    # python_requires=">=3.5",
    license='MIT',
    install_requires=['numpy', 'opencv-python'],
    include_package_data=True,
    # package_data={
        # 'vision_stuff': files,
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # entry_points={
        # "console_scripts": [
            # "shrink_img=vision_stuff:shrink_img_cli",   # to be done
            # "shrink_dir=vision_stuff:shrink_dir_cli",   # to be done
        # ]
    # },
)
