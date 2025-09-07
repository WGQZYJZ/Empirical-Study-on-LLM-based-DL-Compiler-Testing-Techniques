
class Model(torch.nn.Module):
    def __init__(self, weight1=None, weight2=None):
        super().__init__()
        self.weight = torch.nn.Parameter(torch.tensor([5., 6]))
        self.weight1 = torch.nn.Parameter(torch.randn(*self.weight.shape))
        if weight1 is not None:
            self.weight1.data = self.weight + weight1
        else:
            self.weight1.data = self.weight

        self.linear  = torch.nn.Linear(3,2)
        self.conv   = torch.nn.Conv2d(4,50,kernel_size=7, stride=(1,))
        self.norm   = torch.nn.BatchNorm1d(num_features=2)

    def forward(self, x):

        t1  = self.weight # Apply a linear transformation to the input tensor
        t3  = t1 * 0.5     # Multiply the output of the linear transformation by 0.5
        t4  = t3 + other  # Add another tensor to the output of the linear transformation
        t2  = torch.cat([t4,self.weight], dim=1) 
        t6  = self.linear(x)+torch.randn(*self.weight.shape)
        t7  = t2 * x
        t8  = self.norm(x)
 
        return t3
