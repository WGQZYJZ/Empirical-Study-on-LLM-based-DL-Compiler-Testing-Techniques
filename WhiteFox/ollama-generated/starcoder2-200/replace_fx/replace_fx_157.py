

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.dropout(x1, 0.5), torch.rand_like(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32, 64) # A dummy input of size [batchsize x dim]
__output__  = m(x1)
