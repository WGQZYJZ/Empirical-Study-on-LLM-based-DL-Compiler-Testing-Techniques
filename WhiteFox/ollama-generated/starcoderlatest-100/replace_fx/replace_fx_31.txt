
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(x1, dtype=torch.float64)
        v2 = torch.nn.functional.dropout(v1, p=0.5) # Use random number generator to dropout the value between 0 and 1 with probability of 0.5
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
