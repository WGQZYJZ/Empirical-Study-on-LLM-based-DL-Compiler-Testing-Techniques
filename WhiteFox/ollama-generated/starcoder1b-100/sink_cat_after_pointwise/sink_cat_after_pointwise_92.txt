
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Reshape the tensor as follows: [batch_size, channels, height, width] -> [batch_size * channels, height, width]
        v2 = torch.relu(v1)
        return torch.cat([v1, v2], dim=1)


# Initializing the model
m  = Model()


