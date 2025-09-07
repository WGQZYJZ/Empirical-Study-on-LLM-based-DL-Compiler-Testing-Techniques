
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1).view(-1, 9)
        v2 = torch.relu(v1)
        return self.linear(v2)


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(2, 3)
 x2 = torch.randn(2, 4)
