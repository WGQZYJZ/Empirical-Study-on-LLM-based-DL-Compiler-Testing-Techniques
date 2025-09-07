
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 32, dim=0)
        v4 = [v3 for v3 in v2]
        v6 = torch.cat(v4, dim=0)
        return v6

# Initializing the model
m = Model()

 # Inputs to the model<|end_of_input|>  = torch.randn(1950, 8)
__output__  = m(__inputs__)
