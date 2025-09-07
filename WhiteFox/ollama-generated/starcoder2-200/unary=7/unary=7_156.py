
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 28*28))
        return torch.clamp(v1 + 3, min=0, max=6)/6

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(3, 28 * 28)
 
 __output__  = m(x1)
 
