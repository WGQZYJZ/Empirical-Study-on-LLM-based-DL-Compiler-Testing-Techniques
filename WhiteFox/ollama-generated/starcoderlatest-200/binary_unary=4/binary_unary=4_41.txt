
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
        if other is not None:
            self._other = True 
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self._other = False

    def forward(self, x1):
        v1 = self.linear(x1)
        if not self._other:
            v2 = v1 + torch.zeros_like(v1).fill_(1.0)
            v3 = F.relu(v2)
            