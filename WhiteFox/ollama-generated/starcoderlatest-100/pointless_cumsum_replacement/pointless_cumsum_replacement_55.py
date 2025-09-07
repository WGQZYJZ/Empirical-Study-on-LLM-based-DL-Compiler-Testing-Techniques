
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.full([32, 64], 1)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 0)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 64, 64)
