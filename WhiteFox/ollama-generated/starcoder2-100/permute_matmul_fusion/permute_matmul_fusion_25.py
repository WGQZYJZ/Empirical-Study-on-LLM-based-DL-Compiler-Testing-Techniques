
class Model(torch.nn.Module):
    def __init__(self, p1 = 0., p2 = None):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v1 = x1.permute((1, 0)) # Permutation
        v2 = torch.bmm(v1, x1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1_ = torch.randn(3, 5)
x2 = torch.randn(6, 4, 7) # 4, 3, 9


__output__  = m(x1_)  # Tensor output for forward pass, and the input should be permuted.

__output_without_permuted__  = m(x2)
# Permutation and broadcasting (for 5, 4, 7)


