
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(64 * 5 * 5, 2)
 
    def forward(self, x):
        v = self.conv1(x)
        v = torch.nn.functional.relu(v)
        v = torch.nn.functional.max_pool2d(v, kernel_size=2, stride=2)
        v = torch.flatten(v, start_dim=-2)
        v = torch.flatten(v, start_dim=-1)
        v = torch.relu(self.fc(v))
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
