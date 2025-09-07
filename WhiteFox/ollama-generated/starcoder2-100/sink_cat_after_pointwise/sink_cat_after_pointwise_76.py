
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = torch.relu(x1 * self.linear1.weight + self.linear1.bias)
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2048, 16385, 1792).to('cuda')
