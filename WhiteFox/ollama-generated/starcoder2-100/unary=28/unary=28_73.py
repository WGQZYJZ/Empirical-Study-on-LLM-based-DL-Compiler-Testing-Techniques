
class Model(torch.nn.Module):
    def __init__(self, maxval=255):
        super().__init__()
        self.linear  = torch.nn.Linear(10 * 16 + 3 * 4 + 8 * 9 + 7)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -maxval)
        v3  = torch.clamp_max(v2, maxval)
