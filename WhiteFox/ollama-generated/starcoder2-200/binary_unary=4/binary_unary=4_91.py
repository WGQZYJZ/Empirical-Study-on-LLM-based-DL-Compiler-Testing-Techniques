
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 1)
 
    def forward(self, x1, y1=None):
        v1  = self.linear(x1)
        if y1 is None:
            return v1
        else:
            v3 = v1 + y1
            v4 = torch.nn.functional.relu(v3)
            return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(60, 20)
y1 = x1 * -1

__output__  = m(x1, y1=y1)