
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = torch.clamp_min(v1, min=0) # Clamp the result to a minimum value of zero
         v3 = torch.clamp_max(v2, max=64) # Clamp the result to a maximum value of 64
         return v3


# Initializing the model and its optimizer
m  = Model()
optim  = torch.optim.Adam(params=[p for p in m.parameters()], lr=0.1) 
