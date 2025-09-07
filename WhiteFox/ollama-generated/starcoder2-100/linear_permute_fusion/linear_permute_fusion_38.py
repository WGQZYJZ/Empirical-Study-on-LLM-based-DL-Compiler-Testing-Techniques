
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(0, 3, 4)
        return v2


# Initializing the model
m = Model()
__inputs__ = torch.randn(5,) # input of size 5 is required here, because it's the dimension of torch.nn.functional.linear input tensor


# Inputs to the model