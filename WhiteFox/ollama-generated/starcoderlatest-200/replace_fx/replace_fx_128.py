
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        torch.nn.functional.dropout(x1, 0.5, True)
        t2 = torch.rand_like(x1)
        return t2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
