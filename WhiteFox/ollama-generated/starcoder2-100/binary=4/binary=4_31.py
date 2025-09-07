
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*16*80, 5)
 
    def forward(self, x1):
         v1 = self.linear(x1) + torch.zeros_like(v1)
         return v1

# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(480,32*16*80).reshape(-1,32*16*80)
__output__  = m(x2)
