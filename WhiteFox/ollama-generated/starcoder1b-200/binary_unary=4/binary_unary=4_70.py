
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 32)
 
    def forward(self, x1, other=0):
        return relu(linear(x1) + other)


# Initializing the model
m = Model()
x1 = torch.randn(1, 4)
