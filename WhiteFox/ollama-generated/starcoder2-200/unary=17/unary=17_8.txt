
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
         v1  = self.convT(x1)
         v2  = F.relu(v1)
         return v2

 # Initializing the model
 m = Model2()
 
 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
  __output__  = m(x1)
