

class ConcatModel(torch.nn.Module):
    def __init__(self, dim=0, size=89237465):
        super().__init__()
 
    def forward(self, *inputs):
       t1  = torch.cat(inputs) 
       t2  = t1[:, :dim] 
       t3  = t1[:, (size + 1):]
       t4  = torch.cat([t1], dim=0)
       return [t1 for t in inputs], [t2, t3], [t4]

# Initializing the model
model = ConcatModel(dim=0, size=89237465)


x_list  = [torch.randn(size) for i in range(n)]
x1 = x_list[0]

__outputs__ = model(*x_list)
