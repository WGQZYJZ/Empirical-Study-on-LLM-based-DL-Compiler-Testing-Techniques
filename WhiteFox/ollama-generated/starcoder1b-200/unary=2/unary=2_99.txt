
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.tr_conv = nn.ConvTranspose2d(8, 3, 2, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.5
        v3 = v1 * torch.abs(v1)
        v4 = v1 * torch.log(torch.abs(v1))
        v5 = v2 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v3 * v8
        return self.tr_conv(v9).permute(0, 3, 1, 2)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
