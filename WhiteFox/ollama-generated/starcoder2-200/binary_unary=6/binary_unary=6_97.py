
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = relu(v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
other  = torch.randn(size=(10,)) + 49  # The value of 'other' to use as an input is randomly generated between -5 and 64
x1  = torch.randn(2, 10)
