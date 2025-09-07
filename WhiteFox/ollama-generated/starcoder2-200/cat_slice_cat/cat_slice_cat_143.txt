
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        v1 = torch.cat([x2, x3], dim=0)
        v2  = v1[:, :, :89]
        return v2
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(16, 3, 45, 7)
