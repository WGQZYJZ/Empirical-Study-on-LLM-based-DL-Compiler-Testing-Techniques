
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.matmul(x1, torch.ones((4096), requires_grad=True))
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(576) # x1: query tensor with size [576]
__output__  = m(x1)

