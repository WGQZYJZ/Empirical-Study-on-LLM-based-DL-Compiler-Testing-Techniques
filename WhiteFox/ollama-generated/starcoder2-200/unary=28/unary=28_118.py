
class Model(torch.nn.Module):
    def __init__(self, min_value = 10, max_value= 20):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value) # Clamp the output of the linear transformation to a minimum value
        v3 = torch.clamp_max(v2, max_value) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 3)
__output__  = m(x1)