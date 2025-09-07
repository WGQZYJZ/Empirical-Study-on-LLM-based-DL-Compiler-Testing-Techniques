
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + t  # 't' here is a constant tensor
        v3  = torch.relu(v2)

# Initializing the model
m  = Model()

# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
t    = torch.randn(1, 8, 64, 64)

 # Generating the model output with PyTorch APIs and setting up a control flow statement (if statement or for loop)
with torch.enable_grad():
    torch.autograd.set_detect_anomaly(True)
 
    # The initial tensor generation
    for idx in range(10):
        t = torch.randn(1, 8 * (idx + 2), 64, 64) 
 
    # Generating the model output
    __output__  = m(x1)

