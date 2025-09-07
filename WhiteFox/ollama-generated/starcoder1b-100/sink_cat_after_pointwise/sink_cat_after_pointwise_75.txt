
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1  = x1.permute(0, 2, 1) # Rearrange a tensor to its format with respect to the dimension order of concatenation operation.
        t2  = self.linear(t1)   # Apply linear transformation on the reshaped tensor
        return torch.cat([t1, t2], dim=3) # Concatenate the two tensors

