
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 20)
        self.linear2 = torch.nn.Linear(20, 4)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = clamp(min=0, max=6, l1+3) / 6
        return self.linear2(v2)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
