
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(512, 384)
        self.key    = torch.nn.Linear(512, 384)
        self.scale  = torch.nn.Parameter(torch.zeros(1))
 
    def forward(self, x):
        v1 = F.relu(self.query(x))
        v2 = F.relu(self.key(x))
        v3 = torch.einsum('ni,nj->njc', (v1, v2), dim=-1)
        v4 = torch.div(torch.exp(-self.scale * v3), torch.sum(torch.exp(-self.scale * v3), dim=-1).sqrt())
        return v4


# Initializing the model
m = Model()


