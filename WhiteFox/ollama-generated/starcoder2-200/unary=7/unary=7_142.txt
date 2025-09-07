
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = F.relu6(v1 + 3) * v1 / 4
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
__inputs__ = torch.randn(1, 5)
 
# Model output (prediction). Please add the line below:
