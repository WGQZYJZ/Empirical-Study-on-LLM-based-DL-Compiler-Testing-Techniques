
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(v1 + 3)
        v5 = v2 / 6
        return v5

# Initializing the model
m = Model()

 # Inputs to the model 
 __input__  = torch.randn(4, 100)
 __output__  = m(__input__)
