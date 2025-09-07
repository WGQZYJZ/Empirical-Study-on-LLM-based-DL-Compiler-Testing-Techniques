
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v2 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor
        return torch.rand_like(v2, dtype=torch.float32).size()


m = Model().cuda()

x1 = torch.rand(1000,1000,800).cuda()
x1 = m(x1)