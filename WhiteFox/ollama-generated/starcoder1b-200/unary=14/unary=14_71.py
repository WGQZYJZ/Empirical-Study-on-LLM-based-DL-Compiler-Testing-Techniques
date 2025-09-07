
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * (0.5 + 1e-6).to(torch.bool) # Add a small random number to the output of the transposed convolution
        v3 = v1 * torch.exp(-v2) # Exponentiate the output of the sigmoid function
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
