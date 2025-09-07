
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = torch.nn.functional.relu(v1) # Replace ReLU after concatenation with ReLU before concatenation
        v3 = self.linear(torch.cat([x1, x1], dim=-1))
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
