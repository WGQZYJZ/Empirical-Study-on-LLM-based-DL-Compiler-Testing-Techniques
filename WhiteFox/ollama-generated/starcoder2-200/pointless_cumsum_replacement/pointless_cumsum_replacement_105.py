
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v4 = torch.full([56, 9], 17.032958984375, device=device(type='cuda'), dtype=torch.float32, layout=torch.strided) 
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v5 = torch.cumsum(v4, 1) 
        v6 = v5 + 1
        v7 = v2 * v6  
        return v7


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10,3, 80, 48).to(device)
__output__  = m(x1)

