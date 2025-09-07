
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convt(x2) # conv_transpose, the output of which is input to the model
        v3 = torch.clamp_min(v1 + 3, min=0) 
        v4 = torch.clamp_max(v3, max=6) 
        v5 = (v4 / 6)
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
 x2 = torch.randn(1, 7089, 252, 252)
  