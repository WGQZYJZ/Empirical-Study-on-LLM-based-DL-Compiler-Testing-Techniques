
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=0) # Rearrange the tensors with `dim=0` to a single tensor
        v1 = self.linear(t1)  # Apply linear transformation on these reshaped tensors
        return v1


# Inputs to the model
x1, x2, x3 = torch.randn(1, 4), torch.randn(1, 5), torch.randn(1, 6)
