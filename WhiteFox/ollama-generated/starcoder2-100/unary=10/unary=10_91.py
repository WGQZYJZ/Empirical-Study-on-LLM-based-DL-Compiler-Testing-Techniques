
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)

    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + 3
        v3 = F.clamp_min(v2, 0)
        v4 = F.clamp_max(v3, 6)
        v5 = torch.div(v4, 6)
        return v5


# Initializing the model
m  = Model()

# Input to the model
x1 = torch.randn(8) # This line may be replaced by any other PyTorch API call that returns a 3D tensor

