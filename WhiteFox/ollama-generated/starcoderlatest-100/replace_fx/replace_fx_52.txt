
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5, training=False)
        # Comment out the code below and re-run the command to see how `gm` erases nodes when a fallback function is called instead of a custom PyTorch implementation (such as `torch.rand_like`)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2
