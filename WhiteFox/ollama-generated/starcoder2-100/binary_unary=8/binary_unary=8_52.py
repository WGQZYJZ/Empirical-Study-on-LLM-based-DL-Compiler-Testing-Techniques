
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other  # Add another tensor to the output of the convolution
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
other = torch.randn(1, 48, 60, 90) # Add a new input tensor of the same size and type as "other"
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

