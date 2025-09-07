
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = torch.nn.Linear(50, 784)(x1)
        l2 = l1 * clamp(min=0, max=6, l1 + 3).clamp(min=0, max=6) / 6
        return l2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(50,)

 