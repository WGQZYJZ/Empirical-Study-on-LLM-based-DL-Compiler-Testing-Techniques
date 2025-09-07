
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32 * 64 * 64, 50)

    def forward(self, x1):
        v1 = self.fc1(x1.view(-1, 32 * 64 * 64))
        v2 = torch.nn.ReLU()(v1)

        return v2

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
