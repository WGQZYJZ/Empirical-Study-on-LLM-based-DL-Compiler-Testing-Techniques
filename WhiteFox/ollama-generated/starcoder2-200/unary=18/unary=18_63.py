

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.conv(x2)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.sigmoid(v1)  # Apply the sigmoid function to the output of the convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 64, 50, 80)
x2  = torch.rand(4, 70, 90)

