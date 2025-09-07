
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(32, 5)
 
    def forward(self, x0):
        v1 = self.lin1(x0)
        v2 = v1 + torch.randn(v1.size())
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x0  = torch.randn(5,32)
