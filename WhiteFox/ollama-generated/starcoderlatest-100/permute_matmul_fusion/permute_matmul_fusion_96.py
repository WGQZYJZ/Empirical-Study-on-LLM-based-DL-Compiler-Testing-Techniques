
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, input_tensor_B)  # Permute the input tensor B, and then do a bmm on this permuted tensor with x1 tensor
        v2 = torch.matmul(x1, t1)           # Permutes the input tensor A, and then does matmul on this permuted tensor with t1 tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, 3)
x2 = torch.randn(5, 2, 3)
