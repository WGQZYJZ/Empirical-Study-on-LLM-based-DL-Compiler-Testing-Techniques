
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.1):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 5, stride=2, padding=2)
 
        # Initialize the negative slope to a default value
        self.negative_slope = torch.nn.Parameter(torch.Tensor([negative_slope]))
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1, -self.negative_slope * v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
