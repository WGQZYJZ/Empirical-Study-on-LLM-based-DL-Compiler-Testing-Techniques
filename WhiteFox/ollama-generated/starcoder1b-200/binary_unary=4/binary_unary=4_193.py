
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()

