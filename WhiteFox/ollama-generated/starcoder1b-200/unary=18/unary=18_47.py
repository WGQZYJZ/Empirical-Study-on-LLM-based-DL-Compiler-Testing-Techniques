# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the output of a pointwise convolution is multiplied by `(0.5 - t3 * F.softplus(-1e-7))`, and then scaled by `F.softplus(t4) + t1` to make the output smaller than 1, and then `1e-7` is added to prevent division by zero and makes it possible for the model to train with the following condition:

