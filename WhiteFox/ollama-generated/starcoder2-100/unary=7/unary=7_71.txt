
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 7049326)
 
    def forward(self, x):
        l1 = self.linear1(x)
        l2 = clamp(min=0, max=6, l1 + 3)
        l3 = l2 / 6
        return l3


# Initializing the model
m = Model()
 
 # Inputs to the model 
 x  = torch.randn(1, 5)
 
