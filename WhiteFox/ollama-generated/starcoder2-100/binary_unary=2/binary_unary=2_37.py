
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1) - torch.Tensor([0.4,0.,0.,])
        v2  = F.relu(v1)
        return v2


# Initializing the model