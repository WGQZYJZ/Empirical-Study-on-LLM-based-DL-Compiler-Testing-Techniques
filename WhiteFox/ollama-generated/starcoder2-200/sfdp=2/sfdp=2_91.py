
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(30, 12)
        self.key   = torch.nn.Linear(30, 48)
        self.value = torch.nn.Linear(695, 7 * 3)
 
    def forward(self, x):
         return torch.einsum('ab,bc->ca', [x, torch.cat([self.query(), self.key()])])

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(7*3)
__output__  = m(x1)

