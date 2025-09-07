
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         x2 = torch.rand_like(x1).detach()  # Apply dropout on the input tensor without backprop
         y1 = torch.nn.functional.linear(x2)
         return y1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3,4)
__output__  = m(x1)