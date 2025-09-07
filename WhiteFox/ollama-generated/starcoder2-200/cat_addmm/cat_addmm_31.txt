
class Model(torch.nn.Module):
    def __init__(self, dim = 32):
        super().__init__()
 
        self.fc1   = torch.nn.Linear(4 * 64 ** 2, dim)
        self.fc2   = torch.nn.Linear(dim, 8)
        self.relu0 = torch.nn.ReLU()
        self.bn    = torch.nn.BatchNorm2d(3)
 
    def forward(self, x):
        input  = self.bn(x)
        out1a  = self.fc1(input)
        out1b  = out1a + 0.5 * out1a  # Multiply the output of fc by a constant factor 
        out2   = self.relu0(out1b)
        out3   = torch.addmm(x, 0.7978, x)
 
        return out3, out2

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(64 * 4 * 64 * 64, device='cuda', dtype=torch.float32)

# Initializer 
def init(m):
    if isinstance(m, (torch.nn.Linear)):
        torch.nn.init.xavier_uniform_(m.weight)
 
for p in m.modules():
    if hasattr(p, 'bias'): 
        nn.init.constant_(p.bias, 0.)

m = Model() # Initialization function

# Initializer 
def init(m): 
    if isinstance(m, (nn.Linear)):
        torch.nn.init.xavier_uniform_(m.weight)
    for p in m.parameters():
        print(p.data)
 
# Output of forward pass
model_output = m(x).sum()

