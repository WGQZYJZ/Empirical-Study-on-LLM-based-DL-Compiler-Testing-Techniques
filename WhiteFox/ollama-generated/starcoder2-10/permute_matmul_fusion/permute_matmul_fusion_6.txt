
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1 .permute(0, 2, 1)
        v2  = torch.bmm(v1, self._perm_tensor(x2)) # Permute the input tensor B and perform a batch matrix multiplication.
        return v2

    def _perm_tensor(self, t):
       return permute_t = t.permute(0, 3, 4, 5)

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(batch_size, 6, 7) # Batch size is the 0th dimension of input tensors A and B in this example.
x2  = torch.randn(batch_size, 5, 4, 3)


# Expected outputs from the model
__output__  = m(x1, x2).shape  # The output is a tensor with shape (0th dimension of input tensors A and B, 3rd dimension of input tensors A, 4th dimension of input tensors B - 2, 5th dimension of input tensors B)
