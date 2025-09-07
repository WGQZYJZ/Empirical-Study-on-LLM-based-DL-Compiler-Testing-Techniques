
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.nn.functional.conv2d(x1, weight)  # Fused conv + BN layer
        return output

# Inputs to the model
x1 = torch.randn(1, 3, 5, 5)
