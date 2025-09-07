
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp(v1, min=-5, max=5)
        v3 = torch.clamp(v2, min=0, max=10)
        return v3


# Initializing the model and setting minimum and maximum values
m = Model()
m.conv_transpose.weight.data.fill_(0.75) # Minimum value for the weight parameter
m.conv_transpose.bias.data.fill_(-2) # Minimum value for the bias parameter

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
