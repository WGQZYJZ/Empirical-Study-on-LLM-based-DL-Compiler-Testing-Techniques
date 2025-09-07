
class Model(torch.nn.Module):
    def __init__(self, shape1: torch.Size=(3,), shape2: torch.Size=(4, 5), dim=0) -> None:
        super().__init__()

        self.linear = torch.nn.Linear(*shape1, *shape2)

    def forward(self, x1):
        v1 = x1.permute(dim + 1, 0) # permute along dim axis to make it as 3D
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        return v2


# Initializing the model
m = Model()

x1  = torch.randn(500, 4, 50)
x2 = torch.rand(*x1.shape[:dim+1], *x1.shape[dim:]) # generate the other input tensors

__output__  = m(x1)

