
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1, other=None):
        if other is None:
            v1 = self.linear(x1)
            return v1
        else:
            v2 = self.linear(x1) + other # Add another tensor to the output of the linear transformation
            return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 10)
other_tensor = torch.rand(1, 3)
