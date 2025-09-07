
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 6, 8, 8)
input2 = torch.randn(1, 7, 4, 4)
input3 = torch.randn(1, 9, 8, 8)
input4 = torch.randn(1, 5, 4, 4)
