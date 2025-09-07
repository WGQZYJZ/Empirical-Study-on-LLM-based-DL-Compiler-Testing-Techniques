
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64, 10)
 
    def forward(self, x1):
        v1 = x1
        v2 = self.linear(v1)
        return v2

