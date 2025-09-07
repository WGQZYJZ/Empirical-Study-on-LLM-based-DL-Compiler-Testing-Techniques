
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.linear = torch.nn.Linear(size * 3 + 2, size)

    def forward(self, x1):
        v1 = x1[:, : -4]
        v1 = torch.cat([v1[None], v1[-3][-5:], v1[0]], dim=-2).reshape(-1, self.linear.weight.shape[-2])
        return v1 @ self.linear(v1) + 7


# Initializing the model with a small input size (2,4)
m = Model(size=2)

# Inputs to the model (a batch of 3 tensors)
x1 = torch.randn(3, 5, 30, device="cuda")

