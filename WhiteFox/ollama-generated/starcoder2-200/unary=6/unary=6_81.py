
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v1 * v4
        v6  = v5 / 6
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1)

# Input tensor for the previous model
torch.save(__input__, 'model_inputs/previous.pt')

# Input tensor for the new model
__input__   = torch.randn(1024, 3, 65, 65).cuda()
torch.save(__input__, 'model_inputs/new.pt')