
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 3)
        self.linear_2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Swap the last two dimensions of x1 tensor for input tensor A
        v2 = torch.nn.functional.linear(v1, self.linear_1.weight, self.linear_1.bias) # Apply linear transformation to A's permuted tensor
        w1 = x2.permute(0, 2, 1) # Swap the last two dimensions of x2 tensor for input tensor B
        w2 = torch.nn.functional.linear(w1, self.linear_2.weight, self.linear_2.bias) # Apply linear transformation to B's permuted tensor
        v3 = torch.bmm(v2, w2) # Matrix multiplication of two tensors using the batched matrix multiplication (BMM).
        return v3


# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 3, 2)
