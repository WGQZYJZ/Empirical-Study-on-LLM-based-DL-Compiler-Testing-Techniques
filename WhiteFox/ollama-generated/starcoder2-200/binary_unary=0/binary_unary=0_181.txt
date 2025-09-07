
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2  = v1 + other # where `other` is an input tensor
        v3  = torch.relu(v2) # where `other` is an input tensor
        return v3

# Initializing the model
m = Model()
__output__  = m(x1)

# Inputs to the model
other = torch.randn(7, 80)  # this input tensor is used only in the `Model.forward` function above
x2 = torch.randn(5, 3, 64, 64)
 

