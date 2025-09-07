
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = torch.nn.Parameter(torch.tensor(negative_slope))
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1, -self.negative_slope * v1)
        return v2


# Initializing the model with a negative slope of 0.3
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
