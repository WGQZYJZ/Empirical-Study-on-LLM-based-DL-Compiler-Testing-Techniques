
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 42)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v3  = relu(v2 + other)
        return v3


# Initializing the model and specifying 'other' value. Please do not modify this!
m = Model()
other = torch.rand(42, requires_grad=True)
m.apply_(lambda m: setattr(m, 'other', other))

# Inputs to the model 
x1  = torch.randn(30, 10) 

__output__  = m(x1)

