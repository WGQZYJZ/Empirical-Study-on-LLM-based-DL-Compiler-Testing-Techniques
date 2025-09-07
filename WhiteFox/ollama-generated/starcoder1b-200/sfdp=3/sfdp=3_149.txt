
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1) * 0.5
        v3  = torch.softmax(v1, dim=-1).mul(0.7071067811865476)
        v4 = v2 * v3
        return v4


# Initializing the model
m = Model()

