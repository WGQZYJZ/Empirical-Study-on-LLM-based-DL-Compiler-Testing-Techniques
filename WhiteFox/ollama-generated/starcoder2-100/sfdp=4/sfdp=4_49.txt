
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = x1
        return v

# Initializing the model
m  = Model()

# Inputs to the model