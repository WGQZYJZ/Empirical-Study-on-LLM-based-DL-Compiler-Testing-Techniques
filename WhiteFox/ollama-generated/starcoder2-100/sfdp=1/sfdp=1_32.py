
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(32, 48) # A linear layer with 48 output channels
        self.layer2 = torch.nn.Linear(48, 64) # A linear layer with 64 output channels

    def forward(self, x):
    	v1 = self.layer1(x)
        v2 = self.layer2(v1)
        return v2

# Initializing the model