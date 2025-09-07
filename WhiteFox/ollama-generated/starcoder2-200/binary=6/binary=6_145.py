
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 - 'other' 
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1024,)
__output__  = m(x1)

