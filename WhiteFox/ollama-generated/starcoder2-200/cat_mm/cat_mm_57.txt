
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v3  = torch.cat([v1] * len(x2)) # Concatenate the result of matrix multiplication along dimension 0 by length of x2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
i1, i2  = [torch.randn(48) for _ in range(len(x2))] # Dummy list for input tensors with equal lengths

__output__  = m(*[i1] * len(i1), *[i2])

