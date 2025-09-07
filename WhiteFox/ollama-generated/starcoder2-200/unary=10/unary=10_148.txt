
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       l1 = torch.nn.functional.linear(x1) 
       l2 = 0 + l1 
       l3 = torch.nn.functional.clamp_min(l2, min=0) # clamped_min(input, min, max, out=None)
       l4 = torch.nn.functional.clamp_max(l3, max=6)# clamped_max(input, min, max, out=None)
       l5 = 1 / 6
       return l2 * l5
