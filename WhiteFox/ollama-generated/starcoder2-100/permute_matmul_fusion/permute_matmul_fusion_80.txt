
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1, (0, 3, 1)) 
        v2 =  torch.permute(x2,(0, 3, 1)) 
        return torch.bmm(v1, v2)

# Initializing the model
m  = Model()

# Inputs to the model 
x1 = np.random.rand(50).reshape((50, 1, 1, 49))  # shape (50, 1, 1, 49)
x2 = torch.randn(50, 3, 3)                       # shape (50, 3, 3)
