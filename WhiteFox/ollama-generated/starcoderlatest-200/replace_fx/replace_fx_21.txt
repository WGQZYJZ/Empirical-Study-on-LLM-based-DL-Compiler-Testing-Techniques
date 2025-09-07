
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.3, training=True)
        v2 = torch.rand_like(v1, dtype=torch.float64, device=device)
        return v2


# Initialization of the model
m = Model()

# Inputs to the model (on CUDA device)
x1 = torch.randn(1, 2, 2, device=device).contiguous().to(dtype=torch.float32)
