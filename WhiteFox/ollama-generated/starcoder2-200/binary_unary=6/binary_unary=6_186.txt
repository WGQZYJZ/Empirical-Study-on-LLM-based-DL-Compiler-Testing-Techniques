
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(32, 8)
        v1 = torch.randn(32, 8)
        v5 = v0 - other
        return torch.relu(v5).cuda()


# Initializing the model with some constant 'other' and GPU enabled.
m  = Model().cuda()
# Input tensor on the CPU.
x1 = torch.randn(32, 8)
 
# Inputs to the model
