
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = torch.nn.functional.dropout(x1, 0.5) # This is a dropout
        t2  = torch.rand_like(t1, dtype=torch.float32) # This is a random tensor

        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 5, requires_grad=True)
__output__  = m(x1)

