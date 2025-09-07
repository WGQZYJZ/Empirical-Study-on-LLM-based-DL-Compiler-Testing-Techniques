
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return (v1 - 5).sum()


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(32, 64)
