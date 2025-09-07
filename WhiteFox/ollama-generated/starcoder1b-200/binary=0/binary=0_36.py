
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other_tensor is not None:
            other = torch.Tensor(*other_tensor).to('cuda')
            assert other.ndim == 2 and other.shape[0] % 2 == 0
            self.conv.weight = other

    def forward(self, x1):
        return self.conv(x1) + other  # Add another tensor to the output of the convolution


# Initializing the model
m = Model()
other_tensor = (1,)
