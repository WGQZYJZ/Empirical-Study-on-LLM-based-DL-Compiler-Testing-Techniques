
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=2, output_padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return sigmoid(v1)


# Inputs to the model
input_tensor = torch.randn(2, 8, 3, 64, 64)
