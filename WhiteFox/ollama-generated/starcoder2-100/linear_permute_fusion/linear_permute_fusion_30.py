
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(0, 3, 1) # <-- Change 1 to the actual dimension which you want to swap here.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 512, 6000)
