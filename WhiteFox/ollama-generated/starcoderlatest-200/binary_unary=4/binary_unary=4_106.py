
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64 * 64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32 * 32))
        return F.relu(v1 + x1.view(-1, 8 * 64 * 64))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
