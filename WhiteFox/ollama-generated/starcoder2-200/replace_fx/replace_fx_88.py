
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1) # replace torch.rand_like -> torch._lowmem_rand_like
        v3 = x1[:, :5] 
        v4  = torch.nn.functional.dropout(v3, p=0.7) # replace dropout -> lowmem_dropout 
        return [v2, v4]


# Initializing the model:  
m = Model()
x1 = torch.randn(8,5,3)


