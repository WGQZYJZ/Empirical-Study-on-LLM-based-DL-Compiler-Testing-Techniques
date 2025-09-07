
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = self.relu(v1 + other)
        else:
            v2 = self.relu(v1)
        return v2


# Initializing the model
m  = Model()
other_tensor = torch.randn(3, 64)
