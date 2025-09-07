
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        t1 = self.linear1(v1)
        v2 = t1.view(*t1.shape[:-2] + (-1,))  # Reshape the concatenated tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


