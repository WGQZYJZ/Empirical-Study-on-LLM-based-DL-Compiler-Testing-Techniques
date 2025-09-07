
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
        self.other  = 4
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other # Subtract 'other' from the output of the linear transformation
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
__input_to_model__ = torch.randn(1, 8).detach() # Other input to the model
 
# Initializing another model that uses `other` in its forward pass as a parameter. The first and second inputs must be different tensors
m2 = Model(other = __input_to_model__)


# Inputs for the first model
x1  = torch.randn(1,3)
__output__  = m(x1)
 
# Initializing another model that uses `other` in its forward pass as a parameter. The first and second inputs must be different tensors
m2 = Model(other= x1.detach())

