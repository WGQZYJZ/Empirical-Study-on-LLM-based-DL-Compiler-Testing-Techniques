
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320*8*8, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + torch.zeros_like(v1) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 320*8*8) # Generate an input tensor with shape [4, 672]
