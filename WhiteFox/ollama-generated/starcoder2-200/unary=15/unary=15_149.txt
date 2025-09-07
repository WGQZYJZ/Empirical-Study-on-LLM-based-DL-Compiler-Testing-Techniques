
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x): # Please also include all the necessary inputs to Model2 to reproduce __output__
        v1 = self.conv(x)
        v4 = relu(v1) # Add activation function
        return v4
