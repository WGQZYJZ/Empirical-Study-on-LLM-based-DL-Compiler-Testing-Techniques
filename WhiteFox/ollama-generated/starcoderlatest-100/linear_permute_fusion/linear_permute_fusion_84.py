
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, 2, 2)
        t2 = t1.permute(...)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
