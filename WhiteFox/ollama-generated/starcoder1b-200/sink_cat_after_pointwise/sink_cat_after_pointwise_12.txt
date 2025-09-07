
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Reshape after concatenation to remove two dimensions
        # and permute before passing it into linear function
        v1 = x1.view(-1, 4)
        v2 = torch.relu(torch.cat([v1, v1], dim=1).permute(0, 2, 1))
        return torch.relu(self.linear(v2))


# Initializing the model
m = Model()


