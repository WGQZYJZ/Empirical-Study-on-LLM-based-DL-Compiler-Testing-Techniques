
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None):
        v1 = torch.nn.functional.linear(x1)

        if other is not None:
            v2  = v1 + other
        else:
            v2 = v1

# Initializing the model
m2 = Model2()
__output__2a, __output__2b = m2(torch.randn(3)) # outputs will be torch tensors of shape (3,)
__output__2c, __output__2d  = m2(torch.randn(3), other=torch.zeros(3)) # both outputs will be torch tensors of shape (3,), but the value of __output__2a is zero

