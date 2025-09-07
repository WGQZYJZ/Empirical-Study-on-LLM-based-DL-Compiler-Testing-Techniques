
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        v3 = F.relu(v1)
        return v3


# Initializing the model
m = Model()

