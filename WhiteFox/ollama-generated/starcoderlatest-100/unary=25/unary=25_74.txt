
class Model(torch.nn.Module):
    def __init__(self, num_features: int, has_bias: bool = False, negative_slope: float = 0.2):
        super().__init__()
        self.linear = torch.nn.Linear(num_features, num_features + (1 if has_bias else 0), bias=has_bias)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Inputs to the model
x = torch.randn(8, 64, 64)
