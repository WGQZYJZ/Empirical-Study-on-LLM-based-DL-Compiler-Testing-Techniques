
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 10)
 
    def forward(self, x):
        v = self.linear(x) + 3
        return v


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(100, 2048)
