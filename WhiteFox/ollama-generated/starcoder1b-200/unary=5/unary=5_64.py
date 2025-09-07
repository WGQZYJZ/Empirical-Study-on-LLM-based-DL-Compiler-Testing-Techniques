
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv_t(x2) * 0.5
        v3 = self.conv_t(x2) * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4  + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()
x2 = __output__


