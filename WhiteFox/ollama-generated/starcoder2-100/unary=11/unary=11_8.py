
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = self.convtranspose(x1) + 3
        v5 = torch.clamp(v2, 0, 6) / 6 
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 48, 37, 39)
 
