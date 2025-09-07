
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 8 * 2, 1)
 
    def forward(self, x):
        v1 = self.linear(x.view(1, -1))
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 3, 64 * 8 * 2)
