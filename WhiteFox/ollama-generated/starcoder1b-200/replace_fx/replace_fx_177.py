
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Original nodes invoking `torch.nn.functional.dropout` or `torch.rand_like` are erased from the graph here.
        # The original node is then used to generate a random tensor with the same size as input_tensor filled with random numbers and the input tensor.
        return torch.rand_like(x1)

