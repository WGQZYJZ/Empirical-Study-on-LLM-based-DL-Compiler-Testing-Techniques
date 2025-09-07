
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
        self.other = torch.randn(10).cuda()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - self.other
        v3 = F.relu(v2)
        return v3

# Initializing the model
m  = Model().to('cuda')

 # Inputs to the model
x1  = torch.randn(1, 10).cuda()
  __output__  = m(x1)

