
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()

        self.linear1 = torch.nn.Linear(32*64**2//dim, 50)
        self.linear2 = torch.nn.Linear(50, 8)
 
    def forward(self, x):
        v1 = self.linear1(x) 
        v2 = torch.relu_(v1) 
        v3 = self.linear2(v2)

        return v3

m = Model(dim=4).to('cuda')

# Inputs to the model<|end_of_input|>
i = torch.randn(8, 3*64**2//dim).to('cuda') # A 3-dimensional input tensor
o = m(i)

