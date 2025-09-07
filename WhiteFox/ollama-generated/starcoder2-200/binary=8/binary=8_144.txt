
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
        self.other = other
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + self.other # Passing the argument to addition operation as a keyword argument
        return v2

# Initializing model with an additional tensor
other  = torch.tensor([0], dtype=torch.float32)
m      = Model(other)

