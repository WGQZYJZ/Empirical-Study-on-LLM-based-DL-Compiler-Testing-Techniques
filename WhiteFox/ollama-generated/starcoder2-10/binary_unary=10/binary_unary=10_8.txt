
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 12)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
other_tensor = torch.randn(1, 8).type_as(x1)
x1 = torch.randn(1, 64) # input tensor should be different from `x1` defined above
 
__output__  = m(x1)

