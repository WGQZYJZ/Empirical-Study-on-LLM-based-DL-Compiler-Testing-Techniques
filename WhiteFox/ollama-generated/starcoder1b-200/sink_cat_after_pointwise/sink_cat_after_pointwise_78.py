# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the generator for a random tensor is invoked and `v1` is created to store the output of this random tensor, which then becomes the input for the linear operation. The optimization `sink_linear_after_generator` is triggered when such a pattern is detected in the model.


# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where `torch.nn.functional.relu` is invoked on an input tensor, and the output of this function (i.e., `t1`) is then used as the main input to the model. The optimization `sink_relu_after_relu` is triggered when such a pattern is detected in the model.
