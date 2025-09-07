
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other
        return v2


# Initializing the model
m  = Model()

# Input to the model
x1 = torch.randn(3000, 128)
__output__= m(x1)