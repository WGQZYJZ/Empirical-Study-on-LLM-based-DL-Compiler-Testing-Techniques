
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3 = torch.randn([64, 8], requires_grad=True)
        v5 = self.conv(x1)
        v7 = v5 - v3[0] # In a single line of code, this statement is equivalent to torch.addmm(-v3[None, : , None].expand(*v5.shape), x1, 1., out=v8)
        return v4


# Initializing the model