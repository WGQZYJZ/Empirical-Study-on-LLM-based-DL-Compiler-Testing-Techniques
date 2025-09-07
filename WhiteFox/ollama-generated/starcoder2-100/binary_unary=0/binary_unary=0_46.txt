
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor # <- You are to find this line!
        v3  = torch.relu(v2) 
        return v3


# Initializing the model
m  = Model()
other_tensor = 5.0 * torch.randn(8,8).requires_grad_(True)
x1 = torch.randn(1, 3,64,64)
