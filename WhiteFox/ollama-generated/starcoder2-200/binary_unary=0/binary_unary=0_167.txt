
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + torch.randn_like(v1)
        v4 = torch.relu(v2)

        return v4

# Initializing the model
m  = Model()
 
# Input to the model