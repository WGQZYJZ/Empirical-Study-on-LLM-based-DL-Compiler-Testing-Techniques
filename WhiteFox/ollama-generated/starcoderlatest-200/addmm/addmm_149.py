
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        inp = torch.randn(10)
        v1 = torch.mm(x1, inp)  # Perform matrix multiplication on two input tensors
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(32, 48, 64, 64)
