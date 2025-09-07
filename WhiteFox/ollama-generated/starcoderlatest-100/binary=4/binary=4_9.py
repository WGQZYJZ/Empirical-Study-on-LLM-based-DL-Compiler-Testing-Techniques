
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not other is None:
            v2 = v1 + other # Add another tensor to the output of the linear transformation
        else:
            return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
