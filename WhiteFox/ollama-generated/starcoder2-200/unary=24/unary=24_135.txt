
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,kernel_size=[7,7],stride=1)
        self.linear = torch.nn.Linear(9*9*8 ,5 )
        self.linear1 = torch.nn.Linear(5,5)
        self.conv1  = torch.nn.Conv2d(3,4,kernel_size=[6,7],stride=1)
 
    def forward(self, x):

        v0 = conv(x)
        v1 = v0>0
        v2 = v0 * negative_slope
        v3 = torch.where(v1 , v0 , v2)
        v4 = conv1(v3) 
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(1,3,64,64)
 
