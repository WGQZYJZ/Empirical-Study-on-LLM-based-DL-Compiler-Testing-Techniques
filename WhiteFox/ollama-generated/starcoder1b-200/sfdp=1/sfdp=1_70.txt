
class Model(torch.nn.Module):
    def __init__(self, hidden_size=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, hidden_size, 1)
 
    def forward(self, x1, mask=None):
        v = self.conv(x1)
        if mask is not None:
            m = torch.bernoulli(mask).view(*v.shape[0:-1], 1).expand(*v.shape[0:-1])  # Generate a bernoulli tensor with the same shape of the input
            v = torch.mul(m, v)  # Mask out values based on the mask
        return v


# Initializing the model
model = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mask = torch.randn(1, 1, 64, 64).bool()
