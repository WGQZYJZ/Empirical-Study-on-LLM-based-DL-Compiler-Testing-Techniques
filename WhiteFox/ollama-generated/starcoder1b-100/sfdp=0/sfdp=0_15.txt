
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.matmul(v1, self.conv2.weight.transpose(-2, -1)) / self.conv2.weight.pow(2).sum(dim=-1, keepdim=True).sqrt()
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
