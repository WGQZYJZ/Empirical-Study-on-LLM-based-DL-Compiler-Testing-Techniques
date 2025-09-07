
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x2) 
        v2 = torch.zeros((v1.shape[0], 3))
        v3 = v1 + v2
        v4 = torch.relu(v3)

        return v4

# Initializing the model
m = Model()

 # Inputs to the model 
x1, x2 = torch.randn(1, 3, 64, 64), torch.zeros((1000))
__output__  = m(x1)