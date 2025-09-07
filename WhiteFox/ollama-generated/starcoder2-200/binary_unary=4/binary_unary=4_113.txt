
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1  = self.linear(x1)
        v2 = other + v1 # Other is a global tensor. It is added to the output of the linear transformation.
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 784) # Input tensor shape should be (batch_size=50; features/dimensionality of input=784)
other = torch.zeros(50, 20).to(device)

__output__  = m(x1, other=other)


