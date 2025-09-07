
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other=None):
        v0 = self.linear(x1)
        v1 = v0 + other
        v2 = F.relu(v1)
        return v2


# Initializing the model