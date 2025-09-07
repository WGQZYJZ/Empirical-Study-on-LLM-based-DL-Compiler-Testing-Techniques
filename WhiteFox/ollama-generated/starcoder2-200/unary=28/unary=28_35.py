
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(32 * 64, 5)(x1)
        v2  = torch.clamp_min(v1, -0.7)
        return torch.clamp_max(v2, 0.8)


# Initializing the model
m  = Model()


# Inputs to the model
__input__  = torch.randn(1, 32 * 64)

