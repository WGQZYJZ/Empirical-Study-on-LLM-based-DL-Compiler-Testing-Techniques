
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.linear = torch.nn.Linear(2048, 64)
        else:
            self.linear = torch.nn.Linear(3, 64)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

