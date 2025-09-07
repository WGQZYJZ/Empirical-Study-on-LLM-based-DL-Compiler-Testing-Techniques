

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)

    def forward(self, x1):
        v1  = torch.split(x1,[4096],[0]) # split x1 by a size of [4096] along dimension 0. 
        v2  = torch.split(v1[0],split_sizes=[576],dim=3) 
        return v2

# Initializing the model
m  = Model()
__output__  = m(x1)

