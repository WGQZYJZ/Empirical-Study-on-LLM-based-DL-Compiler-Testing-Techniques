
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0, output_padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = sigmoid(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
