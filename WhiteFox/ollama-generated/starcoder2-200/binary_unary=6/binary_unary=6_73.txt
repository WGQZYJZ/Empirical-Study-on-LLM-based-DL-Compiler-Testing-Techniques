
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8192, 3072)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result of the previous operation
        return v3


# Initializing model
m  = Model()
 
# Inputs to the model
x = torch.randn(4, 8192)
other = 0.5
__output__  = m(x)