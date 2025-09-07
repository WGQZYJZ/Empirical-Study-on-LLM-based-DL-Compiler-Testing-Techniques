
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(64, 30)
 
    def forward(self, x1):
        v1 = self.conv(x1) - other 
        v2 = torch.relu(v1) 
        return v2


# Initializing the model