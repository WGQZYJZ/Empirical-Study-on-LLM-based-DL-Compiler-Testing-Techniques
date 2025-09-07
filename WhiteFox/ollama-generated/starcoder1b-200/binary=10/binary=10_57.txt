
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 1)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.cat((v1, self.linear2(other)), dim=-1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, requires_grad=True) # x1 will be modified by m(...)
