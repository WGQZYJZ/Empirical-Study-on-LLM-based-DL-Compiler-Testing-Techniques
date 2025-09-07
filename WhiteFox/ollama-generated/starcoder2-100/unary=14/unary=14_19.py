
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(8, 4, 3, stride=2)
        self.conv2d = torch.nn.Conv2d(4, 6, 5, padding=(0, 1))

    def forward(self, x):
        v1  = self.conv1d(x) 
        v2  = self.conv2d(v1)  
        return v2


# Initializing the model
m  = Model()
 
# Input to the model (input tensor of shape [N x 8 x 4])
x = torch.randn(1, 8, 4)
 
__output__  = m(x)

