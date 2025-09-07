
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[1])
        v2  = torch.mm(x1[2], x1[3])
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = [torch.randn(4, 5),
       torch.randn(5, 6)]
 
