
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = x1.view((...)).permute(...)  # Reshape the concatenated tensor
        return self.relu(v1)


# Initializing the model
m = Model()


