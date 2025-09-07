
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            assert hasattr(other, 'shape') and len(other.shape)==2, "Error in the shape of the `other` tensor. Please make it have exactly two dimensions."
 
    def forward(self, x1):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model
m = Model()
other = torch.randn(2, 3, 64, 64)
