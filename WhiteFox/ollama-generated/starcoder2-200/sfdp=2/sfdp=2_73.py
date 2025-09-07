class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8) # Apply a linear transformation to the input tensor with kernel size (3, 8). The bias is set to zero by default.
        self.linear2 = torch.nn.Linear(7 * 4 + 8, 5, bias=False)  # Apply a linear transformation that takes as an output only the first four columns of the output from the previous layer as the input and has kernel size (7, 5).
    def forward(self, x1):
        v1 = self.linear2(torch.cat([v1_1, v1_4], dim=1)) # Concatenate two tensors along a new dimension.
        return v1
