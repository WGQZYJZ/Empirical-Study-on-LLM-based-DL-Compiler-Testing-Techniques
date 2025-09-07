
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(30, 12)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 30)
 
 # Target output of the model
 target_output  = m(x1)
