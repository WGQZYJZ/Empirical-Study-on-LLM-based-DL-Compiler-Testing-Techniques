
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Replaced with its replacement version (lowmem_dropout and rand_like respectively).
        v1 = torch.rand(x1.shape, device=x1.device, dtype=x1.dtype)  # Generate a random tensor
        return self.linear(v1)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
