
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.rand_like(x1).clone()
        t2  = torch.nn.functional.dropout(v0, p=0.3) # Apply dropout with probability 0.3 to the input tensor.
        return t2


# Initializing and running the model
m  = Model()
x1 = torch.randn(4, 2)
