
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -50)
        v3  = torch.clamp_max(v2,  50)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
__output__  = m(x1)

