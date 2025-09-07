
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([1, 3], 0.5, dtype=torch.float32, layout=torch.strided, device=torch.device("cpu"), pin_memory=False)  # Create a tensor filled with the scalar value 0.5, with the specified dtype, layout, and device
        v3 = v1 * v2
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v3 * v5
        return v6


# Initializing the model
m = Model()


