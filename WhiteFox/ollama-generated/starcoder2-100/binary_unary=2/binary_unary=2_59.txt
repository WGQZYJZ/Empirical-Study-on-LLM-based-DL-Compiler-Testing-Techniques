
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.tensor([0.5], requires_grad=True)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other
        v3  = F.relu(v2)
        return v3


# Initializing the model