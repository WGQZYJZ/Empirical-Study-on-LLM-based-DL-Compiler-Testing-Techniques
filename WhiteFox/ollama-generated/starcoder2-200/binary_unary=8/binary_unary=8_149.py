
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v2 = self.conv(x1) +  other
        return torch.relu(v2)

 # Initializing the model