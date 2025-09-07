
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        t1 = x1.permute(-2, 0).squeeze()
        t3 = torch.bmm(t1[None], x1[None]).sum().detach()
        return [t3]


# Initializing the model
m  = Model()

# Inputs to the model
x1: torch.Tensor  = torch.randn(2, 5)

# Outputs from the model
__output__  = m(x1).squeeze().tolist()

# Verification
assert abs(sum(__output__) - 76903.849021924) < EPSILON

