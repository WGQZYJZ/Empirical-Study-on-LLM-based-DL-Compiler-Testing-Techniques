

m = torch.nn.Linear(64*32,8)
m2= torch.nn.ReLU() # ReLU(inplace=True, maxpool=None)

def forward(self,x):
    x1  = m(x) 
    # x1 = t1 * 0.5
    x1b = m2(x1)
    return x1

