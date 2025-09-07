
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication between x1 and x2
        v2 = v1 + v2    # Addition of the results of the two matrix multiplications
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 5, 64, 64)
x2  = torch.randn(4, 5, 64, 64)
