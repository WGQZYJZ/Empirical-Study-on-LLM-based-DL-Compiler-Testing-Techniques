
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(16, other)
 
    def forward(self, x):
        v = self.linear(x)
        return v - other


# Initializing the model
m = Model()


