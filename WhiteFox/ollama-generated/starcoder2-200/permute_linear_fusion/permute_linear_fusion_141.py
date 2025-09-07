
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = x1.permute(-3,-4).permute(-3,-5).reshape(-10,) # Permute the input tensor
        v2 = self.linear(v1) # Apply linear transformation to the permuted and reshaped tensor.
        return v2


# Initializing the model