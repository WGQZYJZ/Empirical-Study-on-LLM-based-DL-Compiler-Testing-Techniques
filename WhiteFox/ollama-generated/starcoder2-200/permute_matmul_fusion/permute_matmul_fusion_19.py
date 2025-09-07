
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1.permute(0, 2, 1), weight, bias)  # Apply linear transformation to the permuted tensor A
        v2 = input_tensor.bmm(v1).squeeze()                             # Compute a 3-D matrix multiplication and then squeeze out the first two dimensions of the tensor 
        return v2
