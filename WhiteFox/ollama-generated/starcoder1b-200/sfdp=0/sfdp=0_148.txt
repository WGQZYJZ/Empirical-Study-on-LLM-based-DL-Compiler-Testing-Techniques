
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d((1, 1), (2, 2))
 
    def forward(self, x1):
        # Compute the scaled dot product attention weights
        # between a query tensor q and a key tensor k.

        # We can use any number of keys for each query, since
        # they have the same size. Here we have one so it is fixed.
        hk = torch.ones(x1.shape)
        # Now compute the scaled dot product attention weights.

        # We do not use an inverse square root of the scale
        # factor here as it does not help stabilize the gradients.

        # Do not forget to broadcasting if necessary.

        v2 = self.conv1(x1)  # (batch, channels, length, height)
        v3 = self.pool(v2).transpose(-2, -1).contiguous()  # (batch * height, batch * width, channels)
        # ... and then transpose back to (batch * width, batch * height, channels)

        k2 = self.conv2(v3).transpose(-2, -1).contiguous()  # (batch * width, batch * height, channels)

        return torch.matmul(k2, hk.float())
# Initializing the model
m = Model()


