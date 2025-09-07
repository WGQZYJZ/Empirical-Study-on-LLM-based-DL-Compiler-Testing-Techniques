
class Model(nn.Module):
    def __init__(self, dim_1=0, dim_2=0):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        return torch.cat([
            torch.mm(x1, x2),  # Apply pointwise convolution with kernel size 1 to the input tensors
            torch.mm(x1, x2),
            ...,  # Add a sequence of pointwise convolutions and concatenate along axis=2
        ], dim_2)


# Initializing the model
m = Model()


