
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.where(v1 > 0, v1, (v1 - 0.5) * -0.7071067811865476)  # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
