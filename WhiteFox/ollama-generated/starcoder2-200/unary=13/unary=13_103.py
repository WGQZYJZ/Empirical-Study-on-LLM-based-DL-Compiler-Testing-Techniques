
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 512)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1  = self.linear(x)
        v3  = torch.sigmoid(v1)
        v4  = v1 * v3
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(64, 784)

# Input tensor shape: [batch_size x input_shape]


# Output of the model
__output__  = m(x)

