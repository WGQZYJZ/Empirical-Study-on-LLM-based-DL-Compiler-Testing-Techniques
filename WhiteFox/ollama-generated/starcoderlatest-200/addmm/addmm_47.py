
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        inp = torch.randn(3,3)
        t1 = torch.mm(x1, inp) + inp # Perform matrix multiplication on two input tensors and then add the result to another tensor 'inp'
        return t1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
