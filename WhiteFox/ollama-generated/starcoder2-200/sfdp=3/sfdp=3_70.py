class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): 
        q  = torch.randn([8096, 774], requires_grad=True)
        k  = torch.randn([8096, 3072], requires_grad=True)
        v  = torch.randn([8096, 192])
        query = q.clone()
        key   = k.clone()

        vq = query @ key.transpose(-2,-1).reshape(576*736, -1) / math.sqrt(3072) 
        vq *= scale_factor
        sm = torch.nn.functional.softmax(vq[:, :, :])
        
        dv = sm.clone()
        dv[torch.isinf(dv)]  = 0
        dv[torch.isnan(dv)]  = 1

        value  = dv.matmul(v)
        return value


m  = Model()
x1, x2 = torch.randn([384*576]),   torch.randn([384*736])  # random input

x1[0][:] = -torch.nan
x2[0][:] = -torch.inf
 
__output__  = m(x1, x2)

