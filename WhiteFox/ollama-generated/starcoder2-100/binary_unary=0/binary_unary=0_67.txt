
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + torch.randn_like(v1).requires_grad_(True)
        v3  = self.relu(v2)
        return v3


# Initializing the model