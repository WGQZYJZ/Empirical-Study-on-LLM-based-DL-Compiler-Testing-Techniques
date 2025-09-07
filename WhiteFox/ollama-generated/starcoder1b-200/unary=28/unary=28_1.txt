
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Inputs to the model
input_tensor  = torch.randn(100, 3, 64, 64)
