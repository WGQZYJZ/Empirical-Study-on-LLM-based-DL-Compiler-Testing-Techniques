
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        return torch.mm(x1[0],  x1[1]) + torch.mm(x2[0], x2[1])


# Initializing the model
m = Model()


# Inputs to the model
input1  = [torch.randn(4, 3), None]
input2  = [None,   torch.randn(5, 8)]
__output__  = m(input1) + m(input2)