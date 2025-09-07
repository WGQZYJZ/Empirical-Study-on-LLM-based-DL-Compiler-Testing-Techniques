
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m  = Model()
 
other  = torch.randn(8) # Tensor passed as a keyword argument

# Inputs to the model
x1  = torch.randn(4, 3)
