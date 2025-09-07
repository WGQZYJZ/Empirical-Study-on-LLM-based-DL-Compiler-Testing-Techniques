
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.full((2,), 1)

    def forward(self, t1):
        v1  = self.full[0] * self.full[1]
        v2  = convert_element_type(t1, dtype)
        v3  = torch.cumsum(t2, dim=1)[None]  # [1] is a dimension argument of the cumsum operator
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn((1, 3, 64, 64))
