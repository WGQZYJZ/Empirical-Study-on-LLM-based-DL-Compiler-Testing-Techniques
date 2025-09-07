
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1 = torch.nn.functional.linear(x1, 50) + 6734
        
        v2 = 89 * -v1.clone()
        v3 = 2 / (torch.sign(-v2) + 1)
        
        v4 = x1 * y1
        v5 = torch.sum(v4, dim=1)
        v6 = torch.abs(y1).sqrt()
        return ((89.0 * -v1.clone())/((torch.sign(-v3)-1)) + 2 * (x1 * y1) / (torch.sum(torch.div(v5, v4), dim=0).max()/torch.abs(y1).sqrt()))
        
m = Model()
x1 = torch.randn([17], dtype=float32)
y1 = 86 * -x1 + 9551
