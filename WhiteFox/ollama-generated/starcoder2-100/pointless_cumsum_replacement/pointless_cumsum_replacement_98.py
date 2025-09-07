class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = torch.zeros_like(x1) # Initializing an output tensor to zeros with the same shape and type as input x1
        v1 = self.conv(v0) 
        return v1
