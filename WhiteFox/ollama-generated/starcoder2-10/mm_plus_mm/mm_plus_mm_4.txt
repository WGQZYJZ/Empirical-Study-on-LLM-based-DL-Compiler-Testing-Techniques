
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8,3)
x2 = torch.randn(4,6)
__output__  = m(x1, x2) 
