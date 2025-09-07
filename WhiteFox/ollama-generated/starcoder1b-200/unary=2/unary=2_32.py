
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2dTranspose(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 0.3333
        v4 = v3 * 0.07996144
        v5 = v1 + v4
        v6 = v5 ** 1 / 2
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 100, 100)
