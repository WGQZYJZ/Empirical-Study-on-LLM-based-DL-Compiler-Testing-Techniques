
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 3
        v3  = F.relu6(v2) # clamps the value between -6 and 6
        v4  = v3 * torch.tensor([0.5],dtype=torch.float).to("cuda") 
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 96, 28)
 
 