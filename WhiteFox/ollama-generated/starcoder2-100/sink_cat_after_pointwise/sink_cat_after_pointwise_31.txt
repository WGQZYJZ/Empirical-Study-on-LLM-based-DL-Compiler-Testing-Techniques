
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        v = torch.cat([t1, 2]) # Sink 2 after pointwise op, which is not allowed in `sink_cat_after_pointwise`
        v = v.view(v.shape[-2:])
        return torch.nn.functional.relu(v)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3,4) # A random tensor of size (3,4)
