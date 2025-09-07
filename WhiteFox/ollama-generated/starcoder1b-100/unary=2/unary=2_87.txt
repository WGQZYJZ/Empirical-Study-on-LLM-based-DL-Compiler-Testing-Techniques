
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = torch.log_softmax(v3, dim=-1)
        v5 = v4[0]
        v6 = v5  + 1
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
