
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        return v3 + other


# Initializing the model
m = Model()

