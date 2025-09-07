
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self.conv  # Conv
        v0_out = v0()
 
        other = Variable(torch.randn(1, 3))
        
        v5 = t2 - other  # Sub
        v6 = relu(v5)   # ReLU
        return v7
 
 
