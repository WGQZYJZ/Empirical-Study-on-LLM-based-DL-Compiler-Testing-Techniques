
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.linear = ...

    def forward(self, x1):
        t1  = torch.cat([...], dim=...)  # Concatenate tensors along a dimension
        t2  = torch.cat([...], dim=...)  # Concatenate the two concatenated tensor
        return self.linear(t3)


# Initializing the model
m = Model(...)


