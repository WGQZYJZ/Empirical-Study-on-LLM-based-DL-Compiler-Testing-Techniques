
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).pow_(2)
        v3 = (v1 * v1).sqrt()
        v4 = v3.pow_(2)
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6.abs().sqrt_()
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = (v2 * v9).pow_(2)
        return v10


# Initializing the model
m = Model()


