
class Model(torch.nn.Module):
    def __init__(self, d1=None, d2=None):
        super().__init__()
        self.linear  = torch.nn.Linear(d1 + d2 + 1, 3)

    def forward(self, x1, y1):
        v1  = [x1, y1]
        v2  = self.linear(*v1)
        return v2


# Initializing the model
m  = Model(d1=4, d2=5)


# Inputs to the model
v1 = [torch.randn(3), torch.randn(4)] # First input tensor and second input tensor
