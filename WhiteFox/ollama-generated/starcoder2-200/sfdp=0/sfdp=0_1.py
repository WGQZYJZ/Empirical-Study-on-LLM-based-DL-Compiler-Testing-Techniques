
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1  = torch.nn.Linear(3072, 512)
 
    def forward(self, x1):
        v1  = torch.cat([x1] * 4896, dim=0).view(-1, 3, 32, 32).permute(1, 0, 2, 3)
        v2  = self.layer1(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(4896, 3072).view(-1, 512)
 __output__  = m(x1)
