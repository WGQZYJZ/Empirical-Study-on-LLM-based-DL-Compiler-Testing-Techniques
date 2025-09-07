
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072 * 4, 1)
 
    def forward(self, x): 
        v1 = self.linear(x) 
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model and adding the tensors to the linear transformation module of the model. 
m = Model()
m.other = torch.nn.Parameter(torch.ones((4,3072)))

# Inputs to the model
x1  = torch.randn(16, 3 * 32**2)
__output__  = m(x1)

