
class Model(torch.nn.Module):
    def __init__(self, min_value=-10., max_value=10.):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1


# Initializing the model
m = Model()

