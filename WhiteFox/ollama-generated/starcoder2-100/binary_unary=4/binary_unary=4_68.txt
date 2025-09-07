
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 512)
        self._other  = other
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + self._other
        v3  = F.relu(v2)
        return v3


# Initializing the model with a different constant as input tensor