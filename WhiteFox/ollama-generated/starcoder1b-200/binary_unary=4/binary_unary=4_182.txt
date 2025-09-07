
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 16)
        self.relu    = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.linear(x1) + self.relu(other)
        return v1


# Inputs to the model
input_tensor = torch.randn(2, 3, 64, 64)
