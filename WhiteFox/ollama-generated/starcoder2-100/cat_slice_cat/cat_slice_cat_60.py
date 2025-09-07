
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = [x1] * 2
        v1 += [[0]]
        v2 = []

        for t in range(len(v1)):
            v2.append(torch.cat([v1[t], torch.rand_like(v1[t])]))
            
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = [
    torch.randn(3, 64, 64), 
    torch.randn(3, 80, 57)
]
__output__  = m(*x1)

