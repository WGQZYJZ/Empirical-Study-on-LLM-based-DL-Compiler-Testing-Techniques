
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=0)
        v1 = t1.view(-1, 8).permute(1, 0) # Reshape the concatenated tensor
        t2 = torch.relu(v1)
        v2 = self.linear2(torch.nn.functional.linear(t2, self.linear1.weight))
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 2)
