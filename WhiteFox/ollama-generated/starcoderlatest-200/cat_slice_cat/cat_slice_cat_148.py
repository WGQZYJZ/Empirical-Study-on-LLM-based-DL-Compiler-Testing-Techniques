
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, t2):
        v = torch.cat([t1, t2], dim=1)
        return v
 
 # Inputs to the model
t1 = torch.randn(1, 3, 64, 64)
