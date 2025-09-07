
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v2 = self.linear(x2)
        v3  = torch.sigmoid(v2)
        v5  = v3 * v2 
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(64, 784) # Generate a  random matrix of size (64 x 784) with 0 mean and unit variance for input data
x2 =  m(x1)


