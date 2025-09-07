
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.t_conv = torch.nn.ConvTranspose2d(16, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.gt(v1, torch.zeros(1).float())
        v3 = v1 * 0.1
        v4 = torch.where(v2, v3, -v3)
        v5 = self.t_conv(v4) # Apply transposed convolution to the output of the where function in the previous scenario
        return v5


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
