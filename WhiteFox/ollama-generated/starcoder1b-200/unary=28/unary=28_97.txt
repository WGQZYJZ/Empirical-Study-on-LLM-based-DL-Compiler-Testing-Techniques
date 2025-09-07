
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-8, max_value=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1  # No change here
        v3 = torch.clamp_min(v2, min_value=min_value)  # Clamp the output of the linear transformation to a minimum value
        v4 = torch.clamp_max(v3, max_value=max_value)  # Clamp the output of the previous operation to a maximum value
        return v4


# Initializing the model
m = Model()


