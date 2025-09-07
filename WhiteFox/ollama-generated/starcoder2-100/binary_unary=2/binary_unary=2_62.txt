
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x) + torch.rand_like(v1) * 0.75 - other
        return relu(v1), v6


# Initializing the model