
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, weight=other)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model