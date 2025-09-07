
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
__inputs__ = torch.randn(4096, 3278, 15, 15, 3)
x1 = torch.randn(batch_size, 10)
