
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        out = torch.nn.functional.dropout(input1, p=0.5)  # This will be erased when `fallback_random` is set or running on CPU devices
        return randlike_wrapper(torch.rand_like(input1), 1.)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3)
__output__  = m(x1)
