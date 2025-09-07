
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 16)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1) # Swaps the last two dimensions of the input tensor with the second to last dimension
        t2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return t2

