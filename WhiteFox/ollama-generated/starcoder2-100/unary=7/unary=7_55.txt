

class Model(torch.nn.Module):
    def __init__(self, l1_size):
        super().__init__()
        self.l1 = torch.nn.Linear(320 * 320 , l1_size)
    
    def forward(self, x1):
        v1 = self.l1(x1.reshape(-1))
        v2 = F.clamp(min=0, max=6, input=v1 + 3)
        v3 = torch.div(input=v2, scale=6)
