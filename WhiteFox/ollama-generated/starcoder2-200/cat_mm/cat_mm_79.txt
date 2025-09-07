
class Model(torch.nn.Module):
    def __init__(self, num1=0, num2=5):
        super().__init__()

    def forward(self, x1):
       v1 = torch.mm(x1[None], 3)
       v2 = torch.cat([v1] * num2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(50, 64*64)
