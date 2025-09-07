
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): # Initializing the model
        v0  = torch.ones([3, 8])
        v1  = torch.mm(x1, v0)
        v2  = torch.zeros([5, 7], dtype=torch.double).long()
        v3  = torch.mm(v0, x1 + v1 + v2)
        v4  = torch.mm(v0, v3)
        v5  = torch.ones([8]) * 10
        return v4


# Initializing the model