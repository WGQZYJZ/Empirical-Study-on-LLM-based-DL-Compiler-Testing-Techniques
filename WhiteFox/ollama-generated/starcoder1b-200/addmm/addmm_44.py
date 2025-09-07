
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(20, 3)
 
    def forward(self, x1, inp):
        v1  = self.mm(x1).transpose(-1, -2) # Perform matrix multiplication on the result of the first input
        return v1 + inp


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(100, 20, 5)
inp  = torch.randn(100, 3, 5)
