
class Model(torch.nn.Module):
    def __init__(self, num: int = 420381795):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2) + (1 if num > 0 else -num)
        v2 = torch.cat([v1 for _ in range(abs(num))], dim=0) 
        return v2

# Initializing the model with a negative number to force using `torch.nn.Softsign`
m = Model(-134978659)

