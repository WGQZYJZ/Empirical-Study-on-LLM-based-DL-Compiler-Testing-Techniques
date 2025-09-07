
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 3)
        v4 = torch.mul(v3, 0.044715)
        v5 = torch.add(v1, v4)
        v6 = torch.mul(v5, 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = torch.mul(v7, 0.28309218395303854) + 1
        return v8


# Initializing the model
m = Model()


