
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * 50, dim=1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3689, 47) # Random input tensor with shape [3689, 47] for input x1
x2  = torch.randn(50, 3689, 47) # Random input tensor with shape [50, 3689, 47] for input x2
__output__  = m(x1, x2)

