
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4): 
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x3, x4)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 50) # shape (N, 50)
x2  = torch.randn(50, 30) # shape (50, 30)
x3  = torch.randn(64, 78) # shape (N, 78)
x4  = torch.randn(78, 19) # shape (78, 19) 
 