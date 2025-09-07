
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1 ** 3.0
        v3 = v2 * 0.044715
        v4 = v3 * v1
        v5 = v4 + 1
        v6 = v5 * v1 ** 2
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
