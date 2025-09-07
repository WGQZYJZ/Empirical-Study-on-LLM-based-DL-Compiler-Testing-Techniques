
class Model(torch.nn.Module):
    def __init__(self, conv1=None, bn1=None, conv2=None, bn2=None):
        super().__init__()
        if conv1 is not None:
            self.conv = conv1  # Add a member `conv` to make it available for the functional API pattern.
        if bn1 is not None:
            self.bn = bn1 # Add a member `bn` to make it available for the functional API pattern.

    def forward(self, input_tensor):
        output = self.conv(input_tensor)  # The output of convXd and bnXd should be fused together into a single tensor and stored in this variable.

        if self.bn is not None:
            output = self.bn(output) # The bn layer will track running statistics.

        return output


# Initializing the model
model = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 32, 32)
x2 = torch.randn(2, 3, 64, 64)
