
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = (v1 > 0).float() # Boolean mask where True corresponds to elements greater than zero
        v3  = negative_slope * v1 
        v4  = torch.where(v2 == False, -negative_slope * v1, 0) # When the mask is True use the first value and when it's false, use the second value
        return v4


m = Model(negative_slope=0.5).cuda()


