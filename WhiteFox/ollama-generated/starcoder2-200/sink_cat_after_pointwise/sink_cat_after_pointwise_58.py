
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, 2)
        v3 = torch.relu(v2 + self.linear.weight.view(2))
        return v3

# Initializing the model
m = Model()

 # Inputs to the model