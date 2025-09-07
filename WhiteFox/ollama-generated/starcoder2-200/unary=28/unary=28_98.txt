
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v3  = 99
        v4 = v1
        v5 = 137
 
        v6 = torch.clamp_min(v4,  v3)
        v7 = torch.clamp_max(v6, v5 )
        return v7


# Initializing the model
m  = Model()
 
# Inputs to the model
x2  = torch.randn(10)
