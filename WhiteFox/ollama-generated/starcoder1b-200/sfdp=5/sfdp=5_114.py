
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.norm1 = torch.nn.LayerNorm(8)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
        self.norm2 = torch.nn.LayerNorm(16)
 
    def forward(self, x1):
        w1 = self.conv1(x1).view(-1, 8 * 4 * 4)
        w1 = self.norm1(w1)
        w1 = F.gelu(w1)
        w2 = self.conv2(w1).view(-1, 16 * 3 * 3)
        w2 = self.norm2(w2)
        return torch.sigmoid(w2)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
