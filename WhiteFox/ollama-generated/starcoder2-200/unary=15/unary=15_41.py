
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):

        v1 = self.conv(x1)
        v2=torch.relu(v1)
        return v2

# Initializing the model
m2=Model()


# Inputs to the model 
x2 = torch.randn(30,48,75,75)
__output_2__= m2(x2)


