
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return relu(v)


# Inputs to the model
input_tensor  = torch.randn(1, 8, 64, 64)
