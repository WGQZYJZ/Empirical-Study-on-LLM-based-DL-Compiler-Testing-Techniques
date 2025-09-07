
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = torch.nn.Parameter(torch.tensor([negative_slope]), requires_grad=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Add `requires_grad` to the function so that it returns a Tensor that supports backpropagation. Otherwise an error occurs when computing gradients.
        mask  = (v1 > 0).float().requires_grad_(True)
        v3 = torch.where(mask, self.negative_slope * v1, v1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
