
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 32)
 
    def forward(self, x):
        v1 = self.linear(x) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


