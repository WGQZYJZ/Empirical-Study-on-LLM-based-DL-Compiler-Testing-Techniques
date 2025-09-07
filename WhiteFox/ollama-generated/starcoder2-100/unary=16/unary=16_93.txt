
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*64*10, 5)
 
    def forward(self, x):
        v1 = self.linear(x).reshape(-1, 8, 5)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(2048, 32*64*10)
__output__  = m(x)


