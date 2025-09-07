
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        v1  = torch.mm(x1, y1)
        v2  = torch.mm(z1, w1)
        return v1 + v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3072, 960) # shape=(3072, 960), where 960 is 108*3*3
y1  = torch.randn(960, 512) # shape=(960, 512), where 512 is a fixed value for the multiplication in this pattern
z1  = torch.randn(512, 48) # shape=(512, 48), where 48 is a fixed value for the multiplication in this pattern
w1  = torch.randn(3072, 960) # shape=(3072, 960), where 960 is 3*3*3
__output__  = m(x1, y1, z1, w1)

