
class Model(torch.nn.Module):
    def __init__(self, N):
        super().__init__()
        self.mm  = torch.nn.functional.linear() 
        self.conv2d = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1  = self.mm(x1, x2)
        v2  = torch.cat([v1 for _ in range(N)], dim=0) 
        return self.conv2d(v2)

# Initializing the model
m = Model(5)

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 80, 96)
__output__  = m(x1, x2)

