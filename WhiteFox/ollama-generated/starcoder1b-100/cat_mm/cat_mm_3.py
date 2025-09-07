
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        t2 = [t1] + [t1]*len(x1)  # List concatenation with a specified dimension
        return t2


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 6)
