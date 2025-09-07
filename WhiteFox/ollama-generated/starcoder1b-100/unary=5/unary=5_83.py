# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the output of a pointwise transposed convolution is multiplied by a constant `0.5` and then the output of the transposed convolution is multiplied by another constant `0.7071067811865476`, and then the error function is applied to the output of the transposed convolution, and then `1` is added to the output of the error function, and then the output of the transposed convolution is multiplied by the output of the error function.


# Installation guide
The following commands are for installing on Ubuntu 18.04 with CUDA 10.2:
