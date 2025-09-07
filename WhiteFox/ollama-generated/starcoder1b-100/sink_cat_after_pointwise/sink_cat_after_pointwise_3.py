

# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where a pointwise binary operation (like Add, Mul, Max) is applied on a pointwise convolution output, followed by the linear transformation on the upsampled output. The optimization `sink_binary_conv2d` and `sink_upsample` are triggered when such a pattern is detected in the model.


# Model
class Model(torch.nn.Module):
    def __init__(self, input_channel=3):
        super().__init__()
        self.linear = torch.nn.Linear(input_channel, 4)

    def forward(self, x1):
        return self.linear(x1).view(4, input_channel // 2, input_channel // 2)


# Initializing the model
m = Model()
t1 = x.unsqueeze(...)  # Unsqueeze tensor to an dimension index.
t2 = torch.nn.functional.conv2d(t1, ...)  # Apply a convolution to input tensor and perform linear transformation to output tensor
t3 = torch.cat([tensor1, tensor2, ...], dim=...)  # Concatenate tensors along a dimension

