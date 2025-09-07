
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(49, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2) # The Relu function is used to restrict the output of the linear transformation and subsequent activation functions from being negative
        return v3


# Initializing model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(8, 49)
__output__  = m(x1)