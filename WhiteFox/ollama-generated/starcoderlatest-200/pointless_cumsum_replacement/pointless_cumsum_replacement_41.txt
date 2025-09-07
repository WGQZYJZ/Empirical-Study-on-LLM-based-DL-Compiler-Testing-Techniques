
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.full([x1.size()[0], 1], 1, dtype=torch.int64)
        v2 = convert_element_type(v1, torch.int32)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 64)
