
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1): 
        return torch.split(x1, 80, dim=3)

    def backward(self):
        x = torch.rand(20, 40, 57, 69).cuda()
        y = m(x)

# Initializing the model
m = Model().cuda()

