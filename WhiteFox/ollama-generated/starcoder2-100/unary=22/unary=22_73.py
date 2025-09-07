
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v3 = torch.tanh(v1)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(100, 8)
__output__  = m(x2)

