
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64, 5)
        self.other = torch.nn.Parameter(torch.randn((10,), dtype=torch.float))
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.other[None] 
        return torch.relu(v2)


# Initializing the model
m  = Model()

# Inputs to the model
input_tensor = torch.randn((4, 32 * 64))
