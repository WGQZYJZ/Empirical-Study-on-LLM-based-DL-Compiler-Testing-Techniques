
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([1, 1], 1, dtype=torch.float, layout='cpu', device='cpu', pin_memory=False) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v3 = torch.cumsum(v2, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v3


# Initializing the model
m = Model()


