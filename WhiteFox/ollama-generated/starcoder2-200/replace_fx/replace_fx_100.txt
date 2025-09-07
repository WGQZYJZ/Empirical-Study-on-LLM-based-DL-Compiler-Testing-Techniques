

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x):
        v1 = torch.nn.functional.dropout(x, p=0.5)
        v2 = torch.rand_like(v1).float()

        # This should not trigger the erase_node line
        v3 = torch.nn.functional.dropout(v2, 0.4)

        return self.linear(v1 + x)

# Initializing the model
m = Model().to('cpu')


# Inputs to the model
__input__ = torch.randn(10, 5).float()

# Output of the model on the input tensor above
__output__  = m(__input__)

<end_of_file>

