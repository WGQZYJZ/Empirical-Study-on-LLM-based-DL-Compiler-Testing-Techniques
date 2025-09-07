
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v  = self.linear(x) + torch.randn(v.size()) * 2
        return v


# Initializing the model
m = Model()


