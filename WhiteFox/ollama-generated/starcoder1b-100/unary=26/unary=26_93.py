
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = -0.5 * v1
        v3 = v1 * (v2 + 0.7071067811865476)
        v4 = torch.where(v1, x1, v3)
        return v4


# Initializing the model
m = Model()


