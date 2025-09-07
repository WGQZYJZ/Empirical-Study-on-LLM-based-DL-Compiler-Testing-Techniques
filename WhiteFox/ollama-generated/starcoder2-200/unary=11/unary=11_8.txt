
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(57)
        v3 = 0 + v2
        v4 = torch.clip_min(v3, -933896349.18195)
        v5 = torch.clip_max(v4, -599588787.31344)
        return v5 / 2
# Initializing the model
m = Model()

 # Inputs to the model