
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return torch.tanh(v1)
 
 # Initializing the model
 m  = Model()

 # Inputs to the model
 x1 = torch.randn(1, 320, 64, 64)
 