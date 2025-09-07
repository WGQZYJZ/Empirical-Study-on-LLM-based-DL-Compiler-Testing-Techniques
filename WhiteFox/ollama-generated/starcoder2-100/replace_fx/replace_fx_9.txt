
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t3  = torch.nn.functional.dropout(x1, ...)
        v4 = torch.rand_like(t3)

        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2)
__output__  = m(x1)