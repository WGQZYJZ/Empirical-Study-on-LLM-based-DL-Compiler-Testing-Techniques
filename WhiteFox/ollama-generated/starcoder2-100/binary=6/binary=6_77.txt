
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = v1 - 5.0 # Replace 'other' with an integer
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(48, )
__output__  = m(x1)
