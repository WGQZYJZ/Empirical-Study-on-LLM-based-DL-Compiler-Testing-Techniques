
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 32)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        return v1 + other

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 8)
