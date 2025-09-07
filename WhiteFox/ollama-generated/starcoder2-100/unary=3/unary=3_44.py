
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)

        v6  = v1 * 0.5 # this line is not removed
        v7 = v1 *  0.7071067811865476 
        
        v2 = torch.erf(v7)# this line is removed
        v3 = v2 + 1
        
        v4  = v6  # this line was removed, 
        # and we know that this line can be deleted as it is equivalent to v2*v3, so we do not need to look for it
        
        v5  = v2 * v3
        
        return v5

# Initializing the model
m = Model()

