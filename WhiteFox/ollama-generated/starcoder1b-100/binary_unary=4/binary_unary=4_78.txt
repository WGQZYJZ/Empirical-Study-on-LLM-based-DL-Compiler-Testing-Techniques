
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other   = torch.tensor(0, requires_grad=True)
 
    def forward(self, x1):
        return self.linear(x1) + self.other
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
