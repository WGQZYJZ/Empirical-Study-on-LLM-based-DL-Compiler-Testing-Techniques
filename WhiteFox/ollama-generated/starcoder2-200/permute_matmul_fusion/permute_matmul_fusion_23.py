
class Model(torch.nn.Module):
    def __init__(self, is_mat_mul=True):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1: int or torch.Tensor, x2: tuple[int], is_mat_mul=False): # Permute the input tensor B
        v3  = [] 
        for v in (x1, x2):
            if v > 0 and isinstance(v, int) == True:
                v4  = torch.randn(v).permute()
                v5  = self.linear
                v6  = v3
            else : 
                v7  = []
                for v8 in (x1, x2):
                    if v8 > 0 and isinstance(v8, int) == True:
                        v9  = torch.randn((v, v))
                    elif v8 < 0 or not isinstance(v8, int) : 
                        v9 = torch.randn((4, 5))
                    if is_mat_mul != False and (isinstance(v3[len(v3)-1], tuple) == True):
                        v7 += [torch.bmm(v6[-1], self.linear)] 
                    elif isinstance(is_mat_mul, bool) or not isinstance(v9, torch.Tensor) : 
                        v7  = v5 
                    else : 
                        v7 = torch.matmul
                    v3+= [v7]
        return tuple(v for v in v2 if isinstance(v, int))

# Initializing the model
m  = Model()

