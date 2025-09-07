
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 + 3, 1)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = other + v1
        v3 = torch.relu(v2)
        return v3


# Initializing the model