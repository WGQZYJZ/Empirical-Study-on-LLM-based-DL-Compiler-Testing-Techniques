
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3 = torch.cumsum(x1, 1)
        return v3

# Initializing the model