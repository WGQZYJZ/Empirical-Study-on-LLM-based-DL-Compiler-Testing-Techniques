
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 8, 3)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
