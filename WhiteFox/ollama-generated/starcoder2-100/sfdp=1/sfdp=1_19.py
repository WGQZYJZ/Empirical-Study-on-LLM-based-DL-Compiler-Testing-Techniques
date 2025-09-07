class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.matmul(x1[:, 0:3], torch.Tensor([4]))
        v5 = torch.matmul(v2 + x1[:, 1:], torch.Tensor([5]), beta=6)
        return v5


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 4).repeat(100, 1) * 2 # Input for the dot product function
