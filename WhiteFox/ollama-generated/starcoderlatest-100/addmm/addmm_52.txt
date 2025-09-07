
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.input1 = torch.nn.Linear(8, inp)

    def forward(self, x2):
        v1 = torch.mm(self.input1(x2), self.input2(inp)) + inp
        return v1


# Initializing the model
m = Model(inp=16)

# Inputs to the model
x2 = torch.randn(1, 8, 32, 32)
