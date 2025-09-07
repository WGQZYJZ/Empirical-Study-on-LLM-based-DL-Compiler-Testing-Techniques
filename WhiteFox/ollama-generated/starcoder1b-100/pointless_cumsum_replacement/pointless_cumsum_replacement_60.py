
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([v1.shape], 1, dtype=v1.dtype, layout=v1.layout, device=v1.device, pin_memory=False) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v3 = torch.cumsum(v2, 1)  # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
