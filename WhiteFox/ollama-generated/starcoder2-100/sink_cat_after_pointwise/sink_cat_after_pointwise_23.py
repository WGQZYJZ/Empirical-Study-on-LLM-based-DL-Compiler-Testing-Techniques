
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(..., ...)

    def forward(self, x1):
        v1   = x1 + ... # Some more operations on x1
        v2_a = torch.cat([v1], dim=...) # Concatenate the modified tensor along a certain dimension.
        v3   = self.linear(...)  # Apply linear operation to the concatenated tensor with another user of the reshaped tensor
        v4_a = ... # Some more operations on v2 after applying linear.
        return v1


# Initializing the model