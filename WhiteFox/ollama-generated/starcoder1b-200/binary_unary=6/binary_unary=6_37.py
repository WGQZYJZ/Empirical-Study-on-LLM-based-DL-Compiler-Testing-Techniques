
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2):
        v2 = self.linear(x2) - 0.5
        v3 = relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 8)
