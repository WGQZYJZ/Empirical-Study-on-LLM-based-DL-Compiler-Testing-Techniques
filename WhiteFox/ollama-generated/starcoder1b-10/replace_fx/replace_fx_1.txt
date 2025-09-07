
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.lowmem_dropout(v1, dropout=0.5, training=training)
        v3 = torch.rand_like(v2, dtype=v2.dtype, device=v2.device)
        v4 = self.linear(v3)  # This node will be replaced with a random value that satisfies the requirements of `forward` in model.py:179
        return v4


# Inputs to the model
x1 = torch.randn(1, 2, 2)
