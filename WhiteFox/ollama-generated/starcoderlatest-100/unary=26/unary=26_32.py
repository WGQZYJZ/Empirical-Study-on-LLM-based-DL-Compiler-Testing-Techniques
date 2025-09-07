
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, negative_slope):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * negative_slope
        v4 = torch.where(v1, x1, v2) 
        return v4


# Initializing the model
m = Model()

# Inputs to the model
negative_slope = torch.randn(1, 1, 3, 1, requires_grad=True)
x1 = torch.randn(1, 3, 64, 64)
