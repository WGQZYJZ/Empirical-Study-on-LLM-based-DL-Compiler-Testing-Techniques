
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(input_tensor, ...)  # The nodes invoking torch.rand_like will not be replaced by lowmem_rand_like
        return torch.nn.functional.dropout(x1, p=0.2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4, 5, 6)
