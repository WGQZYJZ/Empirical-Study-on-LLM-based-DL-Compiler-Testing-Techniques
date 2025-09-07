
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v2 = clamp(min=0, max=6, l1 + 3) 
        v3 = v2 / 6 # Divide the output of the multiplication by 6
        return l3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
