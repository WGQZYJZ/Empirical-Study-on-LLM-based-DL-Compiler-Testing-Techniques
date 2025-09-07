
class Model(torch.nn.Module):
    def __init__(self, arg1=234567890, arg2=234567890):
        super().__init__()
        self.arg = (arg1, arg2)

    def forward(self, x1):
        v1  = torch.full([*self.arg], 1, dtype=torch.double, device="cpu")
        v2  = torch.convert_element_type(v1, torch.float64)
        v3  = torch.cumsum(v2, dim=0)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
__input__  = [torch.rand([i]) for i in m.__class__.arg]

# Outputs of the model
__output__  = m(x1)
