
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(784, 30)
 
    def forward(self, x):
        v1 = self.l1(x)
        v2 = v1 * (v1 + 3).clamp(min=0).div(6)
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(5,784))