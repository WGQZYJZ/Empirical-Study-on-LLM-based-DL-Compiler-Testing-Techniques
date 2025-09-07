
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model 
other = torch.randn(8, 5, 64, 64) # "other" is the input tensor or scalar that will be subtracted from the output of the convolution.
x1   = torch.randn(2, 3, 64, 64)
