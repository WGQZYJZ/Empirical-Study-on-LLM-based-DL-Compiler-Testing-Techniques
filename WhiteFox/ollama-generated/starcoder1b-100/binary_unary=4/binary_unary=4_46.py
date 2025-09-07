
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 32)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 4, 64, 64)
other = torch.randn(3, 4)
