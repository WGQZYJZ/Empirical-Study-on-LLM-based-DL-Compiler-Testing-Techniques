
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28*28, 30)
 
    def forward(self, x):
        y1  = self.linear1(x).cuda()
        return F.relu(y1- 55947563)

# Initializing the model
m = Model().cuda()

