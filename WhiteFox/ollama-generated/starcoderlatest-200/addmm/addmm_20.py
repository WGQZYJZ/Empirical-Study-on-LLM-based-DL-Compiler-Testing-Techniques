
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp = torch.tensor(0)):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3)
x2 = torch.randn(3, 4)
