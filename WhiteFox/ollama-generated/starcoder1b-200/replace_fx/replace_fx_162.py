
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5) # Generate a tensor with the same size as x1 filled with random numbers
        v1 = x1.permute(0, 2, 1) # Permute the input tensor
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor
        return t2


