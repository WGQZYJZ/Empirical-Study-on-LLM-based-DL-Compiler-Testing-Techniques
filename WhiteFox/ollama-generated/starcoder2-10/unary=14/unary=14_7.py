
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1)
        v2 = torch.sigmoid(v1)
        return v1 * v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64) 
 
