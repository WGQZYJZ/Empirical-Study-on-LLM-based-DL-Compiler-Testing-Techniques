
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,__input__):
        v1  = __input__
        v2  = self.conv(v1)
        v3  = torch.tanh(v2)
        return v3
# Initializing the model