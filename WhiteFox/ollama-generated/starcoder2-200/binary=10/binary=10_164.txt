
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = torch.nn.Linear(in_features=x1.shape[-1], out_features=other.shape[-1])(x1)
        v2  = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model