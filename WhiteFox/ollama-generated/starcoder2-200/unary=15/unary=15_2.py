
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)  
        v4 = F.relu(v1)  # Relu is part of PyTorch, so it does not need to be added as a layer
        return v4

# Initializing the model