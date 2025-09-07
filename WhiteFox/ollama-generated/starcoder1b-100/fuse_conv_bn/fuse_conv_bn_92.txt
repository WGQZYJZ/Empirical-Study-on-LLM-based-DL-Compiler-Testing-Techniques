
class Model(torch.nn.Module):
    def __init__(self, device=torch.device("cuda" if torch.cuda.is_available() else "cpu")):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...) # X can be 1 or 3 representing the dimension of the input tensor.
        self.bn1 = torch.nn.BatchNorm2d(...)
        self.conv2 = torch.nn.Conv2d(...) # X should match with Conv2d
        self.bn2 = torch.nn.BatchNorm2d(...)

    def forward(self, x):  # If the `fuse_conv_bn` optimization is triggered, use these three tensors as inputs to the model.
        output = self.conv1(x)  # Use convolution layer (torch.nn.Conv2d), store the output tensor in v1.
        if self.training:
            with torch.no_grad():
                output = self.bn1(output)  # BatchNorm layer uses running statistics to track mean and variance across batch.
                output = self.conv2(output)  # Use convolution layer (torch.nn.Conv2d), store the output tensor in v2.
        else:
            with torch.no_grad():
                output = self.bn1(output)  # BatchNorm layer uses running statistics to track mean and variance across batch, and updates its statistics based on `output`.
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 320, 640)
