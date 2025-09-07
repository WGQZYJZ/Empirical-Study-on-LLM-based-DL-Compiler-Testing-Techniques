
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(64, 3)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model()


