
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 9, 1, stride=1, padding=0)
    
    def forward(self):
        v1 = self.conv1(x1) 
        v2 = torch.softmax(v1, dim=-3)
        v4 = self.conv2(v2)
        return v4


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64) 
 __output__  = m().to(torch.device('cpu'))


