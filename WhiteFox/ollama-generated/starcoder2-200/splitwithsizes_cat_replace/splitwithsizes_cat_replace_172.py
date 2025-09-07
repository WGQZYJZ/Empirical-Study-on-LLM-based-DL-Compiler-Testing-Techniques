
class Model(torch.nn.Module):
    def __init__(self, k1=320, k2=[6]):
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 8, 5)
        self.k1 = k1
        self.k2 = k2
        self.split_tensor = split_tensor
    
    def forward(self):
       ...

