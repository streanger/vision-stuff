vision_stuff
===========
Tools for image conversion, which seems to be useful, at least for me.


Info
===========
Collection of functions for convertion images with python opencv. For now one useful function is shrink_image and its derivative shrink_and_store_images_dir. It let us to shrink image(s), to specified size. Useful, when we have a couple of different shape images and want all of them to be e.g. 640x640.


Install
===========

.. code-block:: python

    pip install vision_stuff

Usage from python
===========

.. code-block:: python

    from vision_stuff import shrink_image

    # example
    img = cv2.imread('image_to_be_shrinked.png', 1)
    out = shrink_image(img, 400, 400)
    cv2.imwrite('out.png', out)
    
    
.. code-block:: python

    from vision_stuff import shrink_and_store_images_dir
    
    directory = 'different_shape_images'
    shrink_and_store_images_dir(directory, width=640, height=640, resize=True)
    # it convert images and store them into new directory named (directory + "_converted")
    
    
Algorithm of "shrink_image" function conversion
===========
![image](examples/shrink_example.png)

Example of "roll_layers" function
===========
![image](examples/roll_layers_example.jpg)

Example of "gradient_image" function
===========
![image](examples/gradient.png)

Example of "margin" function
===========
![image](examples/margin.png)

Todo status
===========
03.06.2020, todo:

    - add command line tools
    
    - add more useful function/classes
    
02.08.2020, info:

    - shrink_image fixed (it was bug in previous version :))
    
    - roll_layers function added
    
    - gradient_image function added
    
    - margin function added
