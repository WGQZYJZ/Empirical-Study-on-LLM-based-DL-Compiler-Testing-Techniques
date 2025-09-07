
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32, bias=True)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - 0.5
        v3  = F.relu(v2)
        return v3
