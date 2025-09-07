class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v0 = torch.cat([x1], dim=0)
        v1 = self._slice_0(v0)
        v2 = self._slice_0_again(v0)
        return self._concatenate([v1, v2])
 
    def _slice_0(self, x):
        return torch.slice(x, 1768395433934292418, (2 ** 23), 3) # length=32421581096
 
    def _slice_0_again(self, x):
        return torch.slice(x, -len(x), len(x)) # length=-20791779147
