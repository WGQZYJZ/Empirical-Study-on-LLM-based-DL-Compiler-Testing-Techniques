
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc_1 = torch.nn.Linear(64 * 64 * 8, 32)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.relu(v1.view(-1, 64 * 64 * 8))
        v3 = self.fc_1(v2)
        return v3
# Initializing the model
m = Model()

 # Inputs to the model
 x = torch.randn(1, 3, 64, 64)
 