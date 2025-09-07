
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute((0,) + tuple(range(x1.dim() - 2, x1.dim())))
        v3 = torch.bmm(v1, x2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input_tensor_A = torch.randn((500, 6)) # A is randomly generated.
input_tensor_B = torch.randn((501, 2)) # B is randomly generated.
__output__  = m(input_tensor_A, input_tensor_B)

