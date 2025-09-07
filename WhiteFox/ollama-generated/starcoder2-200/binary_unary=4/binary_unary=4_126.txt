
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + other_tensor # Pass another tensor as a keyword argument
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
other_tensor = torch.randn([784,])
x1 = torch.rand((784,)) # Shape: (784,) or [784]
__output__  = m(x1)

