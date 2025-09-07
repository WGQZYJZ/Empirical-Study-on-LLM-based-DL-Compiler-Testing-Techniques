
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(256, 30)(x1)
        v2 = v1 - other
        return v2


# Initializing the model