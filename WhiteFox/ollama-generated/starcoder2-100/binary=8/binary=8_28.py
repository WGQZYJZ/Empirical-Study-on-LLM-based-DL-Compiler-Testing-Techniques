
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Conv2d(3, 8, 1)(x1)
        return v1 + other


# Initializing the model with a constant tensor "other" as an argument to the addition operation