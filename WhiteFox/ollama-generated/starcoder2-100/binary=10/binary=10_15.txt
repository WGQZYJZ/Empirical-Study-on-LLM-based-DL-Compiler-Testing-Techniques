
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor using a predefined function
        v2  = v1 + torch.ones(50, 3).cuda() 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5)


__output__  = m(x1)