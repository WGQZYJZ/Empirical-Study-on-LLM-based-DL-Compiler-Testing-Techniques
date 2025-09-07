
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.25)
        t2 = torch.rand_like(x1, dtype=torch.float32) # This is a replacement to `torch.rand_like`
        return (t1 * t2).sum()

# Inputs to the model
x1 = torch.randn(1, 5, 7)
