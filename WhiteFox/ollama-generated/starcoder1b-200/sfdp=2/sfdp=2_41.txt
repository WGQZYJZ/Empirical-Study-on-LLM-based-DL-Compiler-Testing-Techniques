
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 4)
        self.linear2 = torch.nn.Linear(4, 3)
 
    def forward(self, x1, x2):
        # ... do the computation ...
        output  = m.linear1(x1) * m.linear2(output) # ...


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(2, 8, requires_grad=True)
k = torch.randn(3, 4, requires_grad=True)
v = torch.randn(3, 4, requires_grad=True)
