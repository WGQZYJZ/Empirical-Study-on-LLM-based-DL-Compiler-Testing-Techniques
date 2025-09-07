
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.conv_transpose(x1)
        v2 = torch.sigmoid(v1) 
        v3 = v1 * v2 # v1 * 0.5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 14, 14)
