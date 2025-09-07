
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(320 * 64, 8)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 + self.linear1_other  # A tensor other that is specified at runtime
        return v2


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(320, 64).view(-1)
m.linear1_other = torch.zeros_like(m.linear1.weight) # Set a tensor for the "other" argument of self.linear1.forward() as 0
 
