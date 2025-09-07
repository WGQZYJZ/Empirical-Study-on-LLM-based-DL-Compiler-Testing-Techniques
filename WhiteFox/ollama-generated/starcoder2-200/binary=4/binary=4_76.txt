
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 516)
        other = torch.randn(100, 192).view(-1, 4 * 32)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
