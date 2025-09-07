
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-3, max_value=1000000000):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=self.min_value)
        v3 = torch.clamp_max(v2, max_value=self.max_value)
        return v3


# Inputs to the model
input_tensor = 0.5 * torch.randn(1, 4) - 0.25  # Generate a random input tensor
