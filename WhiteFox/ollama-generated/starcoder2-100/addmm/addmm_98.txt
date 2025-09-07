
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v2


# Initializing the model and inputs to the model
m = Model()
 
inp  = torch.randn(3, 4)
__output__  = m(torch.randn(5, 8), torch.randn(8, 6))
