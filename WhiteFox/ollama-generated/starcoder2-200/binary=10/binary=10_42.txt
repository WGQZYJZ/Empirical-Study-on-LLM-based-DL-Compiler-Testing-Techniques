
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v3 = v1 + other # 其他的张量
        return v3


# Initializing the model
m2  = Model()


# Inputs to the model
x1  = torch.randn(4, 5)


