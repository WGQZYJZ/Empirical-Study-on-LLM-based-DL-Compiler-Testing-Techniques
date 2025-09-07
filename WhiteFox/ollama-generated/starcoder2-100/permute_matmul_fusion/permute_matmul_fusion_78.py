
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x1):
        v3 = self.linear(x1.permute(0, 2, 1)) # Permute input tensor first
        return v3

# Initializing the model
m = Model()

