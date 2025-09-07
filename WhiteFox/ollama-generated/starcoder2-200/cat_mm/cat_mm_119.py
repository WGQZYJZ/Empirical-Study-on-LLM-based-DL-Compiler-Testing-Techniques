
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): 
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1 for _ in range(4)], dim=0) # Concatenate the result tensor along a dimension of your choice, here we choose `dim=0`.
        return v2

# Initializing the model
m  = Model()
x1  = torch.randn(8, 3)
x2  = torch.randn(4, 3)
