
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64, 128)
 
    def forward(self, x1):
        v0 = self.linear(x1).reshape(-1, 1)
        v1 = torch.clamp_min(v0, min=10)
        v2 = torch.clamp_max(v1, max=13) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(128 * 64 * 64) # A vector of length 10^9


# Outputs from the model
