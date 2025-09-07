
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, [64], dim=0)[0] # First split with sizes [64].
        v2 = self.conv(v1) * 0.5 # Second multiply all elements in the first tensor by `0.5`.
        v3 = v1 * 0.7071067811865476 # Third multiply all elements in the second tensor by `0.7071067811865476`.
        v4 = torch.erf(v3) + 1 # Fourth add one to the output of the error function.
        v5 = v2 * v4 # Fifth multiply all elements in both tensors by `1`, and finally concatenate them.
        return v5

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
