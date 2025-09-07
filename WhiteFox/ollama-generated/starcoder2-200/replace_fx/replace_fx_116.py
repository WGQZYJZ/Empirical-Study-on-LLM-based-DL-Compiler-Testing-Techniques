
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1, p=0.5)  # Dropout
        v3 = torch.rand_like(v2, dtype=torch.float)   # Use a different distribution instead of the same as the original
        return [v2, v3]


m  = Model()
inputs  = torch.randn(10, 500)
outputs = m(inputs)
