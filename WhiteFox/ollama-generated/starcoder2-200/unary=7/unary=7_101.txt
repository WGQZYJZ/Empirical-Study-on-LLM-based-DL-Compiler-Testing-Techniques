
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        l1  = self.linear1(x1) 
        l2  = l1 * torch.clamp(min=0, max=6, input=l1 + 3) 
        l3  = l2 / 6
        return l3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32)
__output__  = m(x1)

