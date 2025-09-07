
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(16,8)
 
    def forward(self, x1):
        v2  = self.conv(x1)
        return (v2 + torch.zeros_like(v2)).clamp(-30.,5.)

# Initializing the model