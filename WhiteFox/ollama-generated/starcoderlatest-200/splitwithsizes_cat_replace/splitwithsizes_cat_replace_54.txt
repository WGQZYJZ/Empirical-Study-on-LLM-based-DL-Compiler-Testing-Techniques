
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 20, dim=1)
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=1) # If the order of split tensors and the concatenation operation are the same, this optimization will be triggered. 
        return True
