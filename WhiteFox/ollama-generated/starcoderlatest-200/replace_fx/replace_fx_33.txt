
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1, 0.5)  # random function is invoked here, and thus replaced with `lowmem_random`
        v2 = torch.nn.functional.dropout(v1, ...) # dropout function is invoked on the generated tensor
        return self.linear(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
