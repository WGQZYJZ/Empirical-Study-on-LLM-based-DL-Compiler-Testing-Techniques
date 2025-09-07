
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*1024, 512)

    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(8, 64*1024)
other = torch.zeros((512,), dtype=torch.float32)
__output__  = m(x1, other)

