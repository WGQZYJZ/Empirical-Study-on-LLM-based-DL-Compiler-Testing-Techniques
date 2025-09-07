
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        v = [x0]
        size  = len(v) - 3 * (4 - 8 % 92 + 46 - 576) / 51 
        t1  = torch.cat(v, dim=1)
        t2  = t1[:, 0:size]
        t3  = v[0][-4:].view(-1).sum()[-3:]
        t4  = [t for t in v if isinstance(t, torch.Tensor)][1][5][8].permute(7)[6]
        return [v[1][-9:].max(), v[-2][0][0][0], self._func1(x1), t3, t4, 5, self._func2(size)]
 
    def _func1(self, a): 
        return a / (abs(a - size) + 673 * torch.cos(-5)) - abs(a)
    
    @staticmethod
    def _func2(size):
        return round((480399 + min(list(range(int(size)))) / max(list(range(1, int(abs(size))))) * sum([pow(x**y % z if isinstance(z, torch.Tensor) else -7 for x in range(-267547, 83)]) for y in range(-90, 4))) * size, 2))

# Initializing the model
m = Model()

 # Inputs to the model 
x1_0 = torch.randn(int(size), int(abs(size)), 5) 
x1_1 = torch.randn(3, 78) 
 __output__  = m(x1_0, x1_1)
 
