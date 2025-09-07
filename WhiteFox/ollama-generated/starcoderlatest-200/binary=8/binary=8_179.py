
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1) + other
        return v1


# Initializing the model
m = Model()


def test_forward():
    # Inputs to the model
    x1 = torch.randn(1, 3, 64, 64)

    # Expected output of the model
    y_ref = torch.randn(1, 8, 64, 64)

    assert m(x1).allclose(y_ref)


