
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.fc = torch.nn.Linear(6400, 512)
    
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.fc(v1.reshape(-1))
        return v2

# Initializing the model