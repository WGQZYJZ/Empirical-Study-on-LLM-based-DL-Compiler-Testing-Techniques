
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1280, 3)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
torch.manual_seed(0) # To make results reproducible.
x = torch.randn(4, 64*64*3).view(-1, 1280)


__output__  = m(x)