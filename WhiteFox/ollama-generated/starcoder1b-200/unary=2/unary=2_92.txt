
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_tr = torch.nn.ConvTranspose2d(3, 8, kernel_size=2, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_tr(x1)
        v2 = v1 * 0.5
        v3 = v1 * torch.exp(v1) + v1
        v4 = torch.tanh(v3)
        v5 = v4  + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
