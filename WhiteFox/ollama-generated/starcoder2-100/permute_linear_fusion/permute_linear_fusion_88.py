

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v0 = torch.zeros_like(x1)

        v1 = x1[:, :, 0]
        v2 = torch.abs(v1).clone() / (torch.sum(v1) + 1e-8)
        v3 = self.linear.weight * v2 + self.linear.bias[None, :]
        v4 = torch.cat((x1[:, :, 0][..., None], v3), dim=len(self.linear.weight))

        v5 = v0[..., :1]
        v6 = torch.zeros_like(v4)
        v7 = v0[..., -2:]

        return x1, v1, v2, v3, v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 5)

# Main inputs to the model
__input__ = x1

# Outputs of the model from the main input
__output__, _ = m(torch.randn_like(m.__input__))

