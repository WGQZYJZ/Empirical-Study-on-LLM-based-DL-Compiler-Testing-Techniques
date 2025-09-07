
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=0):
        v1 = torch.mm(x1, inp) # Matrix multiplication
        return v1 + inp


# Inputs to the model
m  = Model()
inp = torch.randn(1, 3, 64, 64)
