
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).detach().view(1, -1, 64, 64)  # Detach and view the last dimension to match the specified shape
        v2 = convert_element_type(v1, dtype=torch.float32)  # Convert elements of v1 to float32
        v3 = torch.cumsum(v2, dim=1).view(-1, 64, 64)  # Compute the cumulative sum along dimension `1`
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
