
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1  = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1  = self.mm1(x1[:, :4])
        v2  = self.mm1(x1[:, 5:]) 
        v3  = torch.mm(v1, v2.t()) # Matrix multiplication between the two results of matrix multiplications
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
input1  = np.random.rand(100, 4) + torch.randn(100).expand_as(x[:, :4])
input2  = input1 - 5
input3  = x[:, 5:].clone() # Clone input data to avoid changing it outside the function
input4  = np.random.rand(100, 8) + torch.randn(100).expand_as(x[:, :5])
__output__  = m(torch.cat((input3, x2), dim=1))
