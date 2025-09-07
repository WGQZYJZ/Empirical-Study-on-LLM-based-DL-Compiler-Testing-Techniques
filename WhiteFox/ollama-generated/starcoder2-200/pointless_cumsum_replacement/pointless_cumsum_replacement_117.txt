
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.full([50], 89473, dtype=int) # This is the input tensor for the model. The dimensions of the input tensor are [1, 1].
        v3 = torch.full_like(v2, True)
        v6 = torch.cumsum(v3, 1).long()
        return v6

# Initializing the model
m = Model()

# Inputs to the model
