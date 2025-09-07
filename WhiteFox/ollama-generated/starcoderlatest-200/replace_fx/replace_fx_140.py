
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...)
        t2 = torch.rand_like(x1, ...)
        return ...


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 2, 2)
 