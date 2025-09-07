
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).unsqueeze(-1) # Add -1 to the end of a dimension, so that `bmm` function can compute tensor product.
        v2 = torch.matmul(v1, input_tensor_B).squeeze(-1)

        return self.linear(torch.cat([x2, v2], dim=-1))

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
