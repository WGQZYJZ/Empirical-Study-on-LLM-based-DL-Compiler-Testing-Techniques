
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        v1  = torch.cat([x1, x1], dim=0) # Concatenate two tensors along dimension zero
        t1 = self.conv(v1)   # Apply a convolution operator on the concatenated tensor
        return v2


# Initializing the model
m = Model()

