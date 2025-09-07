
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, x2, y2, z2):
        v1 = torch.mm(x1, y1)
        v2 = torch.mm(z1, z2)
        v3  = v1 + v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(80000, 46, 4975)
y1  = torch.randn(80000, 25000)
z1  = torch.randn(4975, 25000)


x2  = torch.randn(30000, 46, 4975)
y2  = torch.randn(30000, 25000)
z2  = torch.randn(4975, 25000)


__output__  = m(x1, y1, z1, x2, y2, z2)

## Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model. The model should be different from the previous one.

