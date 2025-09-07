
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        v1  = torch.nn.functional.dropout(input1, p=0.5)
        v2  = torch.rand_like(v1) # Note that it will trigger the erase node line if fallback_random is True or the model runs on CPU device.
        return v2

# Initializing the model
m = Model()

