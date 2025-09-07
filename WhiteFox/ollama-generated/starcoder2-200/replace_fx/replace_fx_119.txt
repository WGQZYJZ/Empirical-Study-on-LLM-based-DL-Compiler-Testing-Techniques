
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = torch.nn.functional.dropout(x1)
        t2  = torch.rand_like(t1) # Generate a tensor with the same size as input_tensor filled with random numbers.
        return t1 + t2


# Initializing the model: m
m  = Model()


# Inputs to the model: m(x1), which is the first argument of m's forward method
x1 = torch.randn(3,4)


