
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
         v1  = self.convT(x1) 
         v2  = v1 + 3
         v3  = F.relu6(v2) # ReLU6 is applied to the output of addition operation after clamping
         v4  = v3 * 0.7593869425778971 
         return v4
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
 # Obtain output from the model
 __output__  = m(x1)

