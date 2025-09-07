
class Model(torch.nn.Module):
    def __init__(self, m1):
        super().__init__()
        self.linear = torch.nn.Linear(m1, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A (same with x1).
        v3 = x2.permute(0, 2, 1) # Permute the input tensor B (same with x2).

        v4 = torch.bmm(v1, v3) # Compute bmm of the permuted tensors.

        return self.linear(v4)


# Initializing the model
m = Model(500)


