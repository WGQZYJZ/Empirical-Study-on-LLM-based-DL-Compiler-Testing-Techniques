
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None): # Default 'x2' value None will be ignored later on
        t1  = torch.mm(x1, x2) 
        return t1


# Initializing the model: `forward` method can take an extra argument to ignore it and `None` as a default value will be considered as missing argument 
m  = Model()

# Inputs to the model
inp = torch.randn(4, 5) # The 'inp' tensor is created by us for testing this new scenario
x1  = torch.randn(3, 6).to('cuda:0') 

# Forcing the 'forward' method to ignore this argument
out1a  = m(x1, x2=None) # It will be ignored
assert out1a is None

