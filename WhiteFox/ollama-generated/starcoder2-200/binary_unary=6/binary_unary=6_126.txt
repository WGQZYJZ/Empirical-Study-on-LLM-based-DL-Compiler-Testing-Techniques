
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24, 150)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_value
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()
 
other_value = 0.7 # This is a custom value that was used in the initial example. You may not change this number.
 
# Inputs to the model
x1 = torch.randn(8, 24)


__output__  = m(x1)


