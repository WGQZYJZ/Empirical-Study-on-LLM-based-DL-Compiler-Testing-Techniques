
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v = torch.mm(x1, x2) + 1 # Perform matrix multiplication on two input tensors
        return v

 # Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 3, 64, 64)
inp = torch.randn(3, 8, 50, 50)
