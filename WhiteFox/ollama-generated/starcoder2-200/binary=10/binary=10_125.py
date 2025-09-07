
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 50)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.randn(v1.size())
