
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.ones([3]) + 0.5 # Tensor containing ones with shape (3) and an element added to each value of the tensor in constant `0.5`

        return x1 * v2

m  = Model()
x1 = torch.randn(3, 3)
__output__  = m(x1)

