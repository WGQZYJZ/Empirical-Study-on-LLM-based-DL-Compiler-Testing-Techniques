
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.permute(x1, 0, 2, 1) # Permute tensor_A's last two dimensions to first two positions in this permuted tensor
        v2 = torch.bmm(v1, x2) # Apply bmm transformation on the permuted input tensors

        return v2

# Inputs for the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 3)
x3 = torch.randn(1, 3, 2)


