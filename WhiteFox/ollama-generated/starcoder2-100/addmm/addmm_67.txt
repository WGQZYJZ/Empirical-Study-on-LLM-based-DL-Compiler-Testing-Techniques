
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2)  # Matrix multiplication between two input tensors 'x' and 'inp'
        return (v1 + inp).relu()


# Initializing the model
m  = Model()
 
# Inputs to the model
inp = torch.randn(4096,)   # Tensor that represents the input of size 1 x 4096
x1 = torch.randn(25, 7)    # Input tensor for size 25 x 7
__output__  = m(x1, inp)

