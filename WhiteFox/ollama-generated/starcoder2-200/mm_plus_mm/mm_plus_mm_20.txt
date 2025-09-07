
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1, input2) 
        v3  = torch.mm(input4, v1)
        v5  = v3 + t2 
        return v5


# Initializing the model
m  = Model()
 
 # Inputs to the model
v6  = m(torch.randn(10), input1=tensor([[2.,  8.,  9., ...,  7., -4.,  2.], [3, 11, 5., ..., 8.,  7.,  6.]]), input2=torch.randn(10))

 # Inputs to the model
v6 = m(input3=tensor([[2.,  8.,  9., ...,  7., -4.,  2.], [3, 11, 5., ..., 8.,  7.,  6.]]), input4=torch.randn(10))

 