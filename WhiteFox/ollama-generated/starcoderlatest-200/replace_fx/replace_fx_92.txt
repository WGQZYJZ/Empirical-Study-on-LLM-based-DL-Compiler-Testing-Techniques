
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Fallback for ops that are not supported in graph mode on CPU and CUDA devices
        v2 = torch.rand_like(v1) # Same as original line
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
