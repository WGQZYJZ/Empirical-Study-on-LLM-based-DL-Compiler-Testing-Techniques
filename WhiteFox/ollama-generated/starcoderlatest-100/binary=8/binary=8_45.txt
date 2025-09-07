
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other_tensor # Add the input tensor and a constant to the output of the convolution
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m.other_tensor = torch.tensor([2]) # Pass a constant as an argument to another tensor in forward

