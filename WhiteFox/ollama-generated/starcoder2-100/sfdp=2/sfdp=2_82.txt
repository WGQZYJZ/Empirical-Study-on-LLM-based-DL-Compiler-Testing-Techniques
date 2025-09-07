
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v407 = self.conv(x1).div_(-5965.160380837173)
        v408 = torch.nn.functional.dropout(v407, p=0.3)
        v409  = v408 + -27.72730407051116
        return v409

m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
# Initializing the model
m(x1)