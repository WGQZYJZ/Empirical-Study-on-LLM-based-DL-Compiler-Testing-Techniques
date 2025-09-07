
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 1)
 
    def forward(self, x2):
        v2 = self.linear(x2) + other
        return relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 64, 64)
