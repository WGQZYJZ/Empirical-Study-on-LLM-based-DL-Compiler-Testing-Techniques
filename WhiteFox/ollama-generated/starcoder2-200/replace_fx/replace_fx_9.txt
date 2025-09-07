
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.3) 
        v2 = torch.rand_like(v1, dtype=int)
        return v2


# Initializing the model
m = Model()

# Inputs to the model