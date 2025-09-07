
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_v1 = v1.min() # Get the minimum value of the output of the convolution
        max_v1 = v1.max() # Get the maximum value of the output of the convolution
        return torch.clamp(t1, min_value=min_v1, max_value=max_v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
