
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1280, 7)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)
        return v1 * v2

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(640, 7)

# Outputs of the model
output = m(input_tensor)

