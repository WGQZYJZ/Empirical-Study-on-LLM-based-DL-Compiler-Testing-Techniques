
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 1 / 3)
        v4 = torch.exp(torch.log(v3) / 3)
        v5 = v2 + v4
        v6 = torch.tanh(v5) + 1
        return v6


# Initializing the model
m = Model()


