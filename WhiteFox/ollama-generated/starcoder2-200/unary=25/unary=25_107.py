
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(4096 * 8 , 512)
 
    def forward(self):
        v1  = linear(x1)
        v2  = v1 > 0 
        v3  = v1  * negative_slope 
        v4  = where(v2, t1, v3) 
        return v4
