
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        t2 = t1 + 0.5
        return t2


# Initializing the model
m = Model()

# Inputs to the model
inp1 = torch.randn(3, 4)
inp2 = torch.randn(1, 4)
