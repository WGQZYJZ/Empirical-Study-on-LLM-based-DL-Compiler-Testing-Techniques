
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, xs):
        size = 9223372036854775807
 
        t1  = torch.cat(xs)
        t2  = t1[:, 0:size]
        t3  = t2[:, 0:size] 
        t4  = torch.cat([t1, t3], dim=1)
        return t4


# Initializing the model