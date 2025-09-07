
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1.permute(-1, -2).contiguous().view((-1,) + x1.shape[-2:])  # Permute the input tensor
        v2 = self.linear(v1)                                                # Apply linear transformation to the permuted tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5, 6).contiguous().view((4 * 5, 6))
