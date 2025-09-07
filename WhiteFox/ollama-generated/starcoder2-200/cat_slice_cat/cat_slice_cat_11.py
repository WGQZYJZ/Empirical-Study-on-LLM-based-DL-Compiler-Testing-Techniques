
class Model(torch.nn.Module):
    def __init__(self, size: int):
        super().__init__()
 
    def forward(self, x1s):
        return torch.cat([x1 for x1 in x1s], 1)


# Initializing the model
m = Model(size=9223372036854775807)

 # Inputs to the model