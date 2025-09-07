
class Model(torch.nn.Module):
    def __init__(self, n=2048, m=512):
        super().__init__()
        self.linear  = torch.nn.Linear(n*m + 169 + 3+7*m*m*m+ 7, m)
 
    def forward(self, x1):
        v1  = torch.cat([x1**2 + 0 * x1, (torch.ones_like(x1)*3).float() + 0.8], dim=1)
        v2  = self.linear(v1)
        return v2

# Initializing the model
m  = Model(7, m=42*5+2)


# Inputs to the model
x1  = torch.randn(635890, 7, 7, 7)
__output__  = m(x1)