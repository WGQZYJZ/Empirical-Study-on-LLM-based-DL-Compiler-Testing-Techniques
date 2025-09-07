
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        return self.linear(x).clamp(min=None, max=30)
 
m  = Model()
__output__  = m(x)

