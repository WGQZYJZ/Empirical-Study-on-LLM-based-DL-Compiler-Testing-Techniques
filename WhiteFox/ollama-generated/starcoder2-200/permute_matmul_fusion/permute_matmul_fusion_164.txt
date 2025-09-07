
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3  = x2[None,:,:].permute(0, 2, 1)  # This permutation is to prepare the shape of input tensors.
        v4  = torch.bmm(x1[:, None,:],v3[None]) # Applying bmm to permuted input tensor.
        return v4

# Initializing the model
m = Model()

# Inputs to the model A (dimension: [2, 3]), and B (dimension: [2, 3]). Since we swap two dimensions of one input tensor.
x1  = torch.randn(2, 3)  # Tensor with shape [2, 3]
x2  = torch.randn(2, 3)  # Tensor with shape [2, 3]. Also we prepare the dimension for this input is [2, 1, 3], since the permute function will swap two dimensions of 1d tensor.

__output__  = m(x1, x2)

