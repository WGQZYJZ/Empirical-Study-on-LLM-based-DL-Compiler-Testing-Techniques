

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1): 
        v0   = torch.Tensor([[1., 1., 1.], [4., 5., 6.], [-2., -3., 7.]])
        v1_c = self.conv(x1)
        
        v1_0 = torch.empty(*v0.shape).to(v1_c.device)
        torch.nn.functional.linear_(v1_0, v0, bias=None)
        v2   = v1_c + v1_0

        v3 = F.relu(v2) 
        return v3
