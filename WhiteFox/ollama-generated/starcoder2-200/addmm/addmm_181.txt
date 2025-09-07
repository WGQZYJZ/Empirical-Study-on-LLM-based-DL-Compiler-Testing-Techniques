
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp):
        v1 = torch.mm(x1, x2) + inp 
        return v1

 # Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5000, 784)
x2 = torch.randn(784, 6000)
inp = torch.randn(6000)
 
