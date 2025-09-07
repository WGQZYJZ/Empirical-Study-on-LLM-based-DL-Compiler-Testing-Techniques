
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.dropout(x1)
        v2 = torch.rand_like(v1, x1.dtype)  # Generate a tensor with the same size as input_tensor filled with random numbers
        return v2
