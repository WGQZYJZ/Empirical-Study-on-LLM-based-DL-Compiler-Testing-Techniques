The model that has been modified is shown above, and the inputs are:
![](./examples/models.png)

# How to use
Just run `main.py` in the directory of this project, and it will automatically generate a random input for you (see the examples above), then execute your own code as shown below. You can also check out this demo [here](https://colab.research.google.com/github/yzhao0621/TensorFlow-TensorRT-TRT-demo/blob/master/TRT_ONNX.ipynb).
Note that you can also generate your own input files, and use `main.py` to execute the model on your local machine (just change the `--input_filename` flag with your filename). For more information of command line flags, please refer to the [documentation](https://github.com/facebookresearch/TensorRT-TensorRT-demo/blob/master/TRT_ONNX.ipynb).

# Preparation
This project has been tested on Ubuntu 18.04 and macOS 10.13, with a Nvidia Jetson TX2 board in the machine. Tested on `Python 3.5.2`, `TensorRT 7.2.3.6`.

