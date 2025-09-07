
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 + 3 
        v3  = F.clamp_min(v2, 0) 
        v4  = F.clamp_max(v3, 6)
        return v4 / 6

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 7859, 2805).to(device=device, dtype=torch_type)
 
 # Actual outputs from the model (should be different from the previous one.)
 __output__   = m(x1)
