
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(8196 * 3 + 1024, 5)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        return v1


# Initializing the model
m  = Model2()


# Inputs to the model
x1  = torch.randn(138, 970 + 512) # This tensor is not actually used as input to m
other_tensor  = torch.rand(64, 3 * 3)
__output__  = m(x1, other=other_tensor)


# Model to verify
# Do not remove the previous model
class Model2b(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(8196 * 3 + 1024, 5)
 
    def forward(self, x1):
        v1 = self.lin(x1) # Use the input tensor to initialize a linear transformation 
        return v1


# Initializing the model with the previous input tensor as an argument to the constructor and not just using the input tensor to call the forward function in the constructor
m  = Model2b(other=torch.randn(138, 970 + 512))


# Inputs to the model (don't remove this section)
x1 = torch.randn(138, 970 + 512) # This tensor is not actually used as input to m
__output__  = m(x1)


