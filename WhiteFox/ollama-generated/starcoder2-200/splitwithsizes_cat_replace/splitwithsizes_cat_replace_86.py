
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = torch.split(x1, [496], dim=2)[0] # Split the input tensor into two tensors along dimension 2 using 496
        v2  = self.conv(v1) 
        v3  = torch.cat([v2[i] for i in range(len(v2))], dim=2) # Concatenate the split tensors along dimension 2
        return v3

m = Model()

