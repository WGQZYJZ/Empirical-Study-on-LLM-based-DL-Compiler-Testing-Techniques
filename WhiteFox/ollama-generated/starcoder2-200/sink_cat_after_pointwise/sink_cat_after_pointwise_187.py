
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 2)

    def forward(self, x1):
        t1  = torch.cat([x1, x1], dim=0).view(-1, 2) # Sink- cat after pointwise op
        return torch.relu(t1 @ self.linear.weight + self.linear.bias)

# Initializing the model
m = Model()

