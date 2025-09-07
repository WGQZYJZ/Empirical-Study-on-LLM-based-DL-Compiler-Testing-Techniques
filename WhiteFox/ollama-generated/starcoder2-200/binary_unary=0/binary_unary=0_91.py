
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other_tensor  = torch.randn(10).cuda()
print(m.state_dict().keys())
 
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1.cuda()).cpu()

