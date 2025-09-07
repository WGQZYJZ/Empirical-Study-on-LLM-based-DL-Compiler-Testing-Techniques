
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 128 * 16 + 64 * 32, 512)
 
    def forward(self, x1):
        v1 = torch.cat((x1, x1, x1, x1), dim=-1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 3, 64 * 128 * 16 + 64 * 32)
