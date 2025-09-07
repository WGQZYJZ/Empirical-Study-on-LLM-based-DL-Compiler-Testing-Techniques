
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Linear(20, 3)
        self.conv2 = torch.nn.Linear(48, 56)
        self.conv3 = torch.nn.Linear(72, 9)
 
    def forward(self):
        v1 = torch.empty()
        t1_w  = torch.randn(v1.shape[0], 20).to('cuda') 
        t1_b  = torch.zeros((t1_w.shape[1])).to('cuda') 
        t1   = (torch.mm(self.conv1(x1), t1_w) + t1_b).clone().detach()
        v2 = self.conv2(v1)
        t3  = torch.empty()
        t2 = t1 - t3 # subtract 't3' from the output of the linear transformation
        return t2


# Initializing the model
m = Model()
# Inputs to the model
x1  = torch.randn(4, 5)


# Inputs to the model