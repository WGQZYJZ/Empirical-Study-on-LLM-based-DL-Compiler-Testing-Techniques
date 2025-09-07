
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        return torch.sigmoid(v1)


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
