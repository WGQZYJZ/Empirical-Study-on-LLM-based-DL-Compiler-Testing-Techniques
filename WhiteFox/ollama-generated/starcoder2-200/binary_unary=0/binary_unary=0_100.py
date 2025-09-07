
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + torch.randn(v1.shape).to(x1.device) # Generate a random tensor with the same shape as input 
        v2  = F.relu(v1)
        return v2


# Initializing the model and performing inference using it on input tensors