
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.sigmoid(t1)
        return t2


# Inputs to the model
x  = torch.randn(1, 32)
