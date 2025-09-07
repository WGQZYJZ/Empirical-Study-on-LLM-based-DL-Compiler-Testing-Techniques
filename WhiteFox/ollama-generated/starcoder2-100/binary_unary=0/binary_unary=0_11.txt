
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.other = torch.randn(3)
 
    def forward(self, x1):
        v1  = self.conv(x1) # 5, 9, 64, 64
        v2  = v1 + self.other[None,:,None,:] 
        v3  = torch.relu(v2)# 5, 8, 64, 64
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 