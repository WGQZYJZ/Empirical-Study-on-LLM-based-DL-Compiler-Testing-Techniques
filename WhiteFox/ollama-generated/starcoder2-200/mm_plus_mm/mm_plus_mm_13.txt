
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v3  = torch.mm(x1[0], x1[1])
        v4  = torch.mm(x1[2], x1[3])
        v5  = v3 + v4

        return v5


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = (torch.randn(1,  8),
    torch.randn(8, 64))

x2 = (torch.randn(8, 32),
     torch.randn(32, 64),
      torch.randn(30720 * 1 * 1, 92554))

x3 = [i for i in range(0)]
for i in range(len(x3)):
    x3[i] = np.random.uniform(-1., 1., size=(64, 64)).astype('float') 

x4 = (torch.randn(8,  92554),
     torch.randn(92554, 30720))

__output__  = m([*x1] + x2)

