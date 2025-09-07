
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, dim1):
        return self.conv(x1[:,dim1])

 # Inputs to the model
dim1  = 0
