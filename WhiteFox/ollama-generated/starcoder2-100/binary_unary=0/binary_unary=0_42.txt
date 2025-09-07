
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + torch.ones_like(v1)
 
 
m = Model()

 # Inputs to the model
 x1  = torch.randn(2, 3, 64, 64)
 
 # Model output is used as the input tensor in the following statement:
 