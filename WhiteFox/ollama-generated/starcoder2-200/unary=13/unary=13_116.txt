
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 512)
 
    def forward(self, x):
        v0 = self.linear(x).view(-1) 
        v1 = torch.sigmoid(v0)
        v2 = v0 * v1
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(64,784) # Random 64-dimensional input data with 784 features each
