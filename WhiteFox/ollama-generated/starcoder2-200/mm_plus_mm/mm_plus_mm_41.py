
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.linear = torch.nn.Linear(4900*8,512)
 
    def forward(self,x):
        t1_conv=self.conv(x)
        t2=t1_conv.view(-1,4900*8) #Reshape the 3d tensor into a flat vector of size 4900 * 8
        t3 = self.linear(t2)
        return t3

# Initializing the model
model  = Model()

