
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1, u1, v1, t1):
        v1 = torch.mm(x1, y1) 
        v2  = torch.mm(z1, w1) 
        v3 = torch.mm(u1, v1) + torch.mm(t1, x1)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(640, 590, device='cpu')
y1 = torch.randn(873, 290, device='cuda')
z1 = torch.randn(1453, 273, device='cuda')
w1 = torch.randn(386, 377, device='cuda')
u1 = torch.randn(371, 159)
v1 = torch.randn(702, 734)
t1 = torch.randn(307, 874)

 # Generated model example:

 # Inputs to the model