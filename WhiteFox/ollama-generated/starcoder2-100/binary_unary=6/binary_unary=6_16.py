
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
        self._other  = 0.5
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 - self._other # 'other'
        v3 = F.relu(v2)
