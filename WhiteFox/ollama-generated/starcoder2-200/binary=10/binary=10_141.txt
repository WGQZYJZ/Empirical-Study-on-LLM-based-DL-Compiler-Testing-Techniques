
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x):
        v = self.linear(x)
        return v + torch.randn(v.size())


# Initializing the model
m = Model()


# Inputs to the model