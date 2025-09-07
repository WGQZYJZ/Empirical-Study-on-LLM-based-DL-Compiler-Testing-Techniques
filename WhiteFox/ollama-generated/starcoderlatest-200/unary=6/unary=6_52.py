The model should contain the following pattern:
This pattern characterizes scenarios where the output of a pointwise convolution is added to a constant `3`, then the result is clamped to a minimum of `0` and a maximum of `6` , then the output of the convolution is multiplied by the clamped result, and finally the result of the multiplication is divided by `6`. This pattern is often used in implementations of the ReLU6 activation function, which is a variant of the ReLU activation function that caps the maximum output value at 6.

# Input
