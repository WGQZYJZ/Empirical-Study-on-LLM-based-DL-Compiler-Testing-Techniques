

class Model(torch.nn.Module):
    def __init__(self, dim=32, splits=10):
        super().__init__()
        self.split  = torch.nn.Conv2d(dim, splits*4+1, 3)
 
    def forward(self, input_tensor):
        splitted = torch.split(input_tensor, [1] * (splits-2), dim=0)[0] 
        concatenated = torch.cat([splitted]*5 + [splitted], dim=1).reshape(-1, 4*dim)
        return self.split(concatenated)
