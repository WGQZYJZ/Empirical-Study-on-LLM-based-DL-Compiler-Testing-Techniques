
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(12, 8)
 
    def forward(self, x):
        return self.linear(x) - 1


m = Model()
x = torch.randn(10, 3, 64, 64)
