
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t1 = torch.nn.functional.dropout(x1, 0.5)
         t2 = torch.rand_like(t1, dtype=torch.int8)
         return t2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3)


__output__  = m(x1)