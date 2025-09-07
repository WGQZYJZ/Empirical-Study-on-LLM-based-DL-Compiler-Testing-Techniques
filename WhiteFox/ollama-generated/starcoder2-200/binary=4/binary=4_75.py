

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5120, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor.
        return v1 + other

# Initializing the model
m  = Model()
other= torch.randn(63795800)


# Inputs to the model