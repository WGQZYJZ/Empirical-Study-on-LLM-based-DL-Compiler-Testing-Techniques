
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other):
        v1  = self.linear(x1)
        v2  = v1 + other
        return nn.ReLU()(v2)


# Initializing the model
m = Model()

# Input to the model
x1  = torch.randn(10, 3)
other  = torch.randn(8)
__output__  = m(x1, other)

