
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) # linear transformation of the input tensor
        v2 = v1 + other   # another tensor is added to the output of the linear transformation
        v3 = torch.relu(v2)# ReLU activation function is applied to the result
        return v3
 

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 64)
other  = torch.randn(1, 64)
__output__   = m(x1)

