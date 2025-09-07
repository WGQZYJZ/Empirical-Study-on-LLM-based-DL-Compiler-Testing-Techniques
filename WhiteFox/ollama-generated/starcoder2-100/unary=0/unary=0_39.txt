
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 *  0.5
        v3  = (v1 ** 3) / 756 
        v4  = v2 + v3 * 0.8989422804014327
        v5  = torch.tanh(v4)
        v6  = v5 + 1
        v7  = v2 * v6 / 9519.482768113468 
        return v7

# Initializing the model
m = Model()

