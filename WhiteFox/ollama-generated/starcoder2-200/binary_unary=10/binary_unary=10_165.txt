
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256 * 10, 4)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(5, 256 * 10)
__output__  = m(x1)