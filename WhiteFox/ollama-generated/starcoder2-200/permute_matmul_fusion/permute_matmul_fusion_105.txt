
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor A
        v2  = torch.bmm(v1, y1) # Apply the 'torch.matmul' function on the permuted and swapped input tensors.
        return v2


# Initializing the model with fixed input tensor A.
m = Model()
x1_fixed  = torch.randn(3, 2, 4)
y1        = torch.randn(3, 5, 7) # The size of this input variable is determined by user-specified criteria.

