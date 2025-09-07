
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v2 = torch.rand_like(x1)  # Generate a tensor with the same size as input_tensor filled with random numbers
       return x1 + v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3,4,5)
__output__  = m(x1)