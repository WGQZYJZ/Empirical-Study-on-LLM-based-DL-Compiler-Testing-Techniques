
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3,8)

    def forward(self, x1):
        v20677 = self.conv(x1) 
        v59471 =  torch.clamp_min(v20677, -4.)
        v5830 =   torch.clamp_max(v59471, 12.) 
        return v5830

# Initializing the model
m = Model()

 # Inputs to the model
x1  =  torch.randn(1, 3)
 
