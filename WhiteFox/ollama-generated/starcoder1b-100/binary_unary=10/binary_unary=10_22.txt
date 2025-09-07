
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 32 * 32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn_like(v1)
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(32, 64 * 32, 3)
