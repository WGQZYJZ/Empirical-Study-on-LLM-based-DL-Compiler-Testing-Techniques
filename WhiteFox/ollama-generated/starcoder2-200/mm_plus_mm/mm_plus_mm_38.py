
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):  # Inputs to the model: three 8-dimensional tensors with sizes [20x3] and [50x6]
        v1 = torch.mm(x1, x2) 
        v2 = torch.mm(x3, x4) 
        v3 = v1 + v2  
        return v3

# Initializing the model 
m = Model()

# Inputs to the model
x1 = torch.rand([20, 3])
x2 = torch.rand([50, 6])
x3 = torch.rand([50, 6])
x4 = torch.rand([20, 3])
