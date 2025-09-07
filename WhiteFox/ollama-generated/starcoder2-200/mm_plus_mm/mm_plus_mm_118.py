
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, x2, y2, z2):
        v1 = torch.mm(x1, y1)
        v2 = torch.mm(z1, x2)
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn((500, 784))
input2 = torch.randn((500,))
input3 = torch.randn((784, 500))
input4 = torch.randn((500,))

__output__  = m(input1, input2, input3, input4)

