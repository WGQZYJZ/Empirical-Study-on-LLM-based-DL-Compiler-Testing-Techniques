
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 3, 8, 8)
