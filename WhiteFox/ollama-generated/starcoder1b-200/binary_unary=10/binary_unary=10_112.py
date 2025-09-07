
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        return self.linear(x1) + other


m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 3)
