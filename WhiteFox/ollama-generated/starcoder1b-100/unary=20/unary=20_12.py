
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
