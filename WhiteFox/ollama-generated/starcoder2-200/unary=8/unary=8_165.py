
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.ConvTranspose1d(8, 4, kernel_size=2)
 
    def forward(self, x1):
        v1 = self.conv1d(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v3 * v1
        v5 = v4 / 6 
        return v5

m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 7)
