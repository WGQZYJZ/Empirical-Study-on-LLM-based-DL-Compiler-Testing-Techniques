
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # The 't1' tensor is generated inside of this function
        t2 = torch.rand_like(x1, 0)
        if self.training:
            v2 = t1.view(...)
            v3 = torch.nn.functional.dropout(v2, ...)

        return v3

# Inputs to the model
x1 = torch.randn(1, 4, 8)
