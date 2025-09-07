
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.linear

    def forward(self, x1, x2):
        v1  = mm(x1, x2) 
        return v1 + inp

# Initializing the model
m = Model()

 # Inputs to the model
inp = torch.randn(3,) 
 __input__1__ = torch.randn(4, 5)
 __input__2__ = torch.randn(5, 6)
  __output__  = m(__input__1__, __input__2__)
