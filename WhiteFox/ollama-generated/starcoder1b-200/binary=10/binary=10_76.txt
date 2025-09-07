
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        return self.linear(x) + other

 # Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 10)
