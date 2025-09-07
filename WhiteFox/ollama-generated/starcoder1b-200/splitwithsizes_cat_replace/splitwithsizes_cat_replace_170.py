
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.split(x1, 2, dim=0) # Split tensor on the second dimension (axis=0), and store it in v1 and v2.
        v2 = v1[1] * 2 # Store tensor v1[1] along dim=0 into v3 and compute tensor v2*v3.
        v3 = torch.cat([v1[0], v2], dim=0) # Concatenate tensors together along the first dimension (axis=0).

        return v3


# Initializing the model
m = Model()


