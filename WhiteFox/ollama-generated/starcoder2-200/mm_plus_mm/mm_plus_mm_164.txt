
class Model(torch.nn.Module):
    def __init__(self, m, n):
        super().__init__()
        self.m = torch.nn.Parameter(m)
        self.n = torch.nn.Parameter(n)
 
    def forward(self, x1):
        v1  = torch.mm(x1[:, :3], self.m.permute(0, 1)) 
        v2  = torch.mm(x1[:, 3:], self.m.permute(0, 1)) 
        return torch.cat([v1 + self.n] * 5)


# Initializing the model
m = Model(torch.randn(4, 7), torch.randn(28)).cuda()
# m = Model(torch.randn(3, 6).cuda(), torch.randn(9).cuda()) 
# m = Model(torch.randn(100), torch.randn(5)) 

# Inputs to the model
x1 = torch.rand(8, 4) * torch.randn(28, 7) + 5 # Batch size is different from 8; 1 dimension is smaller than 3. In addition, one of these dimensions in the input tensor is 9 instead of 7
