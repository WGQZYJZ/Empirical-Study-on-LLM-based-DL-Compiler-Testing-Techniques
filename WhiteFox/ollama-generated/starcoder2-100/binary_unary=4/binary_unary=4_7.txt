
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.randn(5) 
        v1  = self.linear1(x1 + other)
        v2  = v1 - 1
        return v2

# Initializing the model and passing in keyword argument to its forward method as input.
m = Model()

