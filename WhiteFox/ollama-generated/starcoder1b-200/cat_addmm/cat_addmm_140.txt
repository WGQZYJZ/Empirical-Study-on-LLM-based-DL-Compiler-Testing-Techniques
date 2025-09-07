
class Model(torch.nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.fc1   = torch.nn.Linear(input_size * 2, hidden_size)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v1 = torch.cat([v1, x], dim=-1)
        v2 = self.fc1(torch.flatten(v1, 1))
        return v2


# Initializing the model
m = Model(64 * 3 * 2, 256)


