
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(20, 40)
 
    def forward(self, x1):
        l1  = self.lin1(x1) 
        l2  = l1 * clamp(min=0, max=6, l1 + 3)
        l3  = l2 / 6
        return l3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 5)
__output__  = m(x1)