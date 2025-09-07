
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1, y1):
        v1  = x1.permute(0, 2, 1)
        v2  = y1.permute(0, 2, 1) # This input tensor needs to be permuted first and then used as the main input for torch.bmm or torch.matmul function
        v3  = torch.nn.functional.linear(v1 + v2, self.linear.weight, self.linear.bias) # Apply linear transformation after adding two tensors
        return v3


# Initializing the model