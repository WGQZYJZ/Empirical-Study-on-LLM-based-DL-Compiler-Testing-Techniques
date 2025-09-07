
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)

    def forward(self, inp):
        v1 = self.conv1(inp)
        v2 = torch.mm(v1, v1)
        return v2 + inp


# Initializing the model
m = Model()


# Inputs to the model
inp1 = torch.randn(48, 3, 640, 960).type(torch.FloatTensor)

__output__  = m(inp1)


