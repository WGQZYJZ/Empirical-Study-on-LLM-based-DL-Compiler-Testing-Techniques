
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...)  # Dropout is invoked here (and the original function node will be erased)
        v2 = torch.rand_like(...)   # Generates a tensor with random numbers
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model
x1 = torch.randn(1, 5, 3)
