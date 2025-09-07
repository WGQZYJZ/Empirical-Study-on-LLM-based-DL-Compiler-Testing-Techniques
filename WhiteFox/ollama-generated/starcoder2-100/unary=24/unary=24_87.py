
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu = nn.ReLU()
 
    def forward(self, x):
        v0   = self.conv(x) 
        v1_1 = (v0 > 0).to(torch.float) # mask for elements >= 0; torch.bool is not supported by `torch.where`
        v2   = -v0 + v0 * v1_1  # where: where(mask, input, other)
        v3_1 = self.relu(v2)
        v4   = v0 * (1.0-v1_1) # multiply the negative values by 0; torch.bool is not supported by `torch.where`
        v5   = -v2 + v4  # where: where(mask, input, other)    
        return v3_1


# Initializing model and inputs to it