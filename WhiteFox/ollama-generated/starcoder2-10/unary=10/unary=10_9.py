
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = torch.nn.functional.linear(x1)
        l2  = l1 + 3 
        l3  = torch.nn.functional.relu6(l2)
        l4  = l3 / 6 # scaled and shifted ReLU6 activation function
        return l4


# Initializing the model: 
m = Model()

# Inputs to the model
x1  = torch.randn(5, 9)
__output__   = m(x1)

