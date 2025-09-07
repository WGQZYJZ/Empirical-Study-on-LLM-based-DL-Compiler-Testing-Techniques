
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t10943, t827675829, size):
        v1  = torch.cat([t10943, t827675829], dim=1)
        v2  = v1[:, :size]
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
t10943  = torch.randn(2, 1024)
t827675829  = torch.randn(10943, 3072)
size  = torch.randint(low=1, high=torch.clamp(len(t827675829)-1, min=-1023, max=1023))
 
__output__  = m(t10943, t827675829, size)

