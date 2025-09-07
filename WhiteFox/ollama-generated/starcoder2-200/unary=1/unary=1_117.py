
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1 = torch.nn.Linear(8*64*64, 32)(x1)
        v2 = v1 * 0.5
        v3 = ((v1 * (torch.zeros_like(v1)+1)).pow(3)) * 0.7978845608028654
        v4 = torch.tanh(v3) + 1
        v5 = v2 * v4

        return v5


# Initializing the model:
m  = Model()

# Inputs to the model:
x1  = torch.randn(1, 8*64*64)

__output__  = m(x1)

