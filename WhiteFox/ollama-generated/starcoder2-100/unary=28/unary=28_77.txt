
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2a = torch.clamp_min(v1, min_value=-3) # Clamp the output of the linear transformation to a minimum value
        v2b = torch.clamp_max(v2a, max_value=5) # Clamp the output of the previous operation to a maximum value
        return v2b

m  = Model()
m.linear = torch.nn.Linear(3*64**2, 1024).cuda()

