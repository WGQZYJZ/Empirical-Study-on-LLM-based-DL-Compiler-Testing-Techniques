
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope 
        v4 = torch.where(v2, v1, v3) # where(condition, True branch, False branch)
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model 
x1 = torch.randn(1000, 32)
__output__  = m(x1)

# End of script

import os
os.system("sh ./run.sh")
