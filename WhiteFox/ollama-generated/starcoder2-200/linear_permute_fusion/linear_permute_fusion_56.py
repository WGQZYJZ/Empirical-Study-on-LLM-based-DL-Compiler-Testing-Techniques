
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3074592 + 1, 3)

    def forward(self, x):
        x  = self.linear(x.permute(1, -1).reshape(-1, 3))
        return x

# Initializing the model
m  = Model()

 # Input to the model: torch.Size([2807])
x  = torch.rand(1, 9504) * 2 - 1

 