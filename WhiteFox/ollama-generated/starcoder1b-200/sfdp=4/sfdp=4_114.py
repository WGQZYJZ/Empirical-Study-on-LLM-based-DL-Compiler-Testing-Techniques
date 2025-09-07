
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.layer_norm = torch.nn.LayerNorm((1, 512))
 
    def forward(self, x1, mask):
        v1 = self.conv(x1)
        v1 = self.layer_norm(v1 * (mask / 2).unsqueeze(-1).unsqueeze(-1))
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
