
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(768, 50)
        self.layer2 = nn.Linear(50, 256)
 
    def forward(self, x1):
        v1 = torch.relu(self.layer1(x1))
        v2 = torch.relu(self.layer2(v1))
        return v2


# Initializing the model
m = Transformer()

# Inputs to the model
x1 = torch.randn(1, 768, 300)
