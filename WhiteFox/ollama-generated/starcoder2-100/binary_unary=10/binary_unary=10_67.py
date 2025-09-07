
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 5)
        self._other = nn.Parameter(
            torch.zeros(3, 6).normal_(mean=0., std=torch.Tensor([0.7894]))
        )
 
    def forward(self, x):
        v1 = self.lin(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3

# Initializing the model