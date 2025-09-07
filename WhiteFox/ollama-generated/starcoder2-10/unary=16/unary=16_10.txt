
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(64*32+10, 5)
 
    def forward(self, x1, x2):
        v1  = x1 * torch.ones_like(x1).to(dtype=torch.float32)
        v2  = x2 + x1
        t   = self.lin(v2) # Apply a linear transformation to the input tensor `v2`
        t0,t1,t2,t3,t4  = t[:,:5], t[:,5:7], t[:,7:8], t[:,8:], t[:,9:] 
        v6  = torch.max(x2, dim=-1) # Apply the max-function to `v`
        return [None]

m0  = Model()

# Inputs to the model<|end_of_input|>
x1, x2 = torch.randn(45), torch.randint(7893,(25,), dtype=torch.int64)


__output__  = m0(x1, x2)