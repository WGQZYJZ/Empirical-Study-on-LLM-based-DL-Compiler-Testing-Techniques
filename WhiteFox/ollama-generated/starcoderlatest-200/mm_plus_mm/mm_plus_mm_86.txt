
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
input_1 = torch.randn(64, 10, requires_grad=True)
input_2 = torch.randn(5, 6, requires_grad=True)
input_3 = torch.randn(9, 11, requires_grad=True)
input_4 = torch.randn(8, 7, requires_grad=True)
