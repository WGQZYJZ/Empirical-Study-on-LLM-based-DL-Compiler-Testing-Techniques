
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(...) # Permute the input tensor A (v1)
        v2 = x2.permute(...) # Permute the input tensor B (v2)

        t3 = torch.bmm(t1, v2) # or torch.matmul(t1, v2)

        return ...  # Return output from computation

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
