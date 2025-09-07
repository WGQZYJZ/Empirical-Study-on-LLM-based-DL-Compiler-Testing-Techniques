

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x1): 
        v3 = x1 + 1 # Addition with a constant value
        t4 = torch.nn.functional.dropout(v3, p=0.5, training=True) # Apply dropout
        v7 = self.linear(t4) # Linear function
        return v7


m = Model()
__output__  = m(torch.rand(1,2))

# Initializing the model
m = Model()
# Inputs to the model
x3 = torch.randn(1024,16)
y3 = torch.randint(100,(1024, 10), dtype=torch.int8) # Create an array with random numbers

