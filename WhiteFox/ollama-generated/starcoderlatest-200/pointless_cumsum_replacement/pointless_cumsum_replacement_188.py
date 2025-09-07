
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1[0].shape[1], 16], 255, dtype=x1[0].dtype)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
__input__ = (torch.randn(2, 3, 10, 10), )
