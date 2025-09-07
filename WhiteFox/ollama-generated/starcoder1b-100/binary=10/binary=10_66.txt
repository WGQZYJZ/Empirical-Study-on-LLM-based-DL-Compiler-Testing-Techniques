
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 16)
 
    def forward(self, x1, other=torch.randn(1, 2048)):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2048)
y = m(x1)
__output__  = y


