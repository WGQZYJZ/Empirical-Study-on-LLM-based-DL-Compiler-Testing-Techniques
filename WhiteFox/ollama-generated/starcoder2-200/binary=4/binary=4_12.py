
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v5 = self.linear(x2) + torch.tensor(2.6936, dtype=torch.float32) 
        return v5

# Initializing the model
n = Model()


# Inputs to the model
x1  = torch.randn(400, 784)
x2  = torch.randn(400, 784) # The input tensor must be different from the previous one.
__output__  = n(x1) + n(x2)

