
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.square(v1)
        v4 = torch.pow(v3, 2.0)
        v5 = v4  * 0.044715
        v6 = torch.sigmoid(v5)
        v7 = v6 + 1
        v8 = v2 * v7
        return v8


# Initializing the model
m = Model()


