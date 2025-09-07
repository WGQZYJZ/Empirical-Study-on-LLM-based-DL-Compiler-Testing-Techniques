
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = self.conv_transpose(x1)
        return torch.sigmoid(v0)

 # Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(32, 8, 56, 56)
