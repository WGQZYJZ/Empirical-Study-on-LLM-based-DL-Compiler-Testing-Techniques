
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2, t3):
        v1 = torch.cat([t1, t3], dim=1)
        return v1

 # Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
x3 = torch.randn(1, 9223372036854775807, 1, 1)
