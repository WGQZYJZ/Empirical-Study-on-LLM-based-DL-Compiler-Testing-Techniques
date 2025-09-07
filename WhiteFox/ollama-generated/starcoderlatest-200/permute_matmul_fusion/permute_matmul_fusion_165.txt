
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A first to apply linear transformation on B. The shape of output tensors after this operation will be (1, 2, 2). Note: permute has a special function called 'moveaxis' that can swap two axes in PyTorch instead of permute function.
        v2 = self.linear(v1) # Apply linear transformation to the permuted tensor. The shape of output tensors after this operation will be (1, 2, 2).
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2) # Shape: (1, 2, 2)
x2 = torch.randn(1, 2, 3) # Shape: (1, 2, 3)
