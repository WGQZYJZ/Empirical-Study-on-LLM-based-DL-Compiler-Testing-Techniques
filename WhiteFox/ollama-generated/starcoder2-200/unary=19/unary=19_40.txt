
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 64)
 
    def forward(self, x1):
        v0 = torch.relu(x1[:, :3].sum(-1)) 
        v1 = torch.sigmoid(v0 - 0.9 * (x1 ** 2).sum(-1) + 1 / 8) 
        v2 = torch.tanh(torch.cat([self.linear(x1), self.linear(torch.relu(x1[:, 3:]) + v0), x1], dim=-1)) 
        v4, v5 = torch.sort(v2, dim=None if v2.dim() == 1 else -1)
        v7 = ((v5 - torch.min(v5).sum(-1)[..., None]) / (torch.max(v5).sum(-1)[..., None] - torch.min(v5).sum(-1)[..., None])) + 0.4 
        return v4, v7

