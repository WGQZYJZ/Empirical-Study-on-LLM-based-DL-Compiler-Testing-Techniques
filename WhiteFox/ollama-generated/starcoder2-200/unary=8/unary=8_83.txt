
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu6(v2)
        v4  = F.relu6(torch.clamp(v3, min=0))
        v5  = torch.div(F.relu6(v4), torch.tensor([6])) 
        return v5

m1 = Model()

 # Inputs to the model
   
x2 = m1(__output__)

print(torch.__version__, torch.Tensor([3]).type())