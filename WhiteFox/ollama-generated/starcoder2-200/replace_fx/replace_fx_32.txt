
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1, p=0)
        v3  = torch.rand_like(v2)

m  = Model()

# Inputs to the model
x1  = torch.randn(16, 8)
__output__  = m(x1)

