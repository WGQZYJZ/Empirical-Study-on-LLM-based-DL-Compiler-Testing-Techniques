
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp, t1, input2=None):
        v1 = torch.mm(t1, t1)  # Perform matrix multiplication on two input tensors
        v2 = v1 + inp
        return v2


# Inputs to the model
inp = torch.randn(8, 16, 50)
t1 = torch.randn(16, 32)
input2 = torch.randn(8, 16)
