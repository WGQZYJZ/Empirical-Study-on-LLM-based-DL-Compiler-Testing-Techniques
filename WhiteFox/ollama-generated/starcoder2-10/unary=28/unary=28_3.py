
class Model(torch.nn.Module):
    def __init__(self, max_value = None):
        super().__init__()

        # Check if the maximum value is provided or not by the user; 
        # If no maximum value is provided, use the default 255 instead of `None` as a maximum value
        self._max_value  = int(max_value) if max_value else 255
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x): 
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, int(-3)) # clamping the value of -3
        v3 = torch.clamp_max(v2, int(self._max_value)) # Clamping max to 255
        return v3


# Initializing the model
m = Model(40)

# Inputs to the model
x1 = torch.randn(1,784)
__output__  = m(x1)