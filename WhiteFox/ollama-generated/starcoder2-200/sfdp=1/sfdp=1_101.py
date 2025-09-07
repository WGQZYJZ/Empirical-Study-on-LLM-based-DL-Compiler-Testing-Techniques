
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(48, 20)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, torch.randn((56 * 7))) + torch.randn(56 * 7).unsqueeze(-1)
        v2  = self.q(v1).squeeze()
        return v2


# Initializing the model