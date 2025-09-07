class Model(torch.nn.Module):
    def __init__(self, minval=0., maxval=32768):
        super().__init__()
 
        self.linear = torch.nn.Linear(512*512, 4)
 
    def forward(self, x1):

        v1  = self.linear(x1)
        v2  = v1 
        v2[:,0] = torch.clamp_min(v2[:,0], minval=0.) # Clamps the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, maxval=32768) # Clamps the output of the previous operation to a maximum value 
        return v3 
