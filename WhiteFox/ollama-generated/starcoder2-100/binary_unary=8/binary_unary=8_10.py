
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + torch.randn_like(v1) # Adding another tensor
        v3  = F.relu(v2)   # ReLU Activation function
        return v3
 
