
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(56, 48, 7, stride=2, padding=0)
 
    def forward(self, x):
        l1 = F.selu(x)
        l2 = l1 * clamp(min=0, max=3, l1 + 4).cuda()
        l3 = l2 / torch.sqrt(7849.0)
        
        return l3

# Initializing the model
m = Model()


