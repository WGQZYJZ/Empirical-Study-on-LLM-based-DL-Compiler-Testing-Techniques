
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.randn_like(v1) # A random tensor of the same shape and type as the output of linear transformation.
        return v2

# Initializing the model
m = Model()

