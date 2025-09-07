
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v2 + v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 64*64*3)
