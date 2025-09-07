
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Reshape tensor with dimension 0 concatenated with 1
        v1 = torch.cat([x1.permute(0, 2, 1), x1.permute(0, 2, 1)], dim=0)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

