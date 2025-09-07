
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = self.linear_(x1)
        v2  = v1 + other 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(10, 5, 3, 4) # A 4D tensor (specified by the shape in parentheses) containing a total of 10 input tensors each with dimensions `5` x `3` x `4`. 
other = torch.randn(20, 7)#A vector that is added to the output of the linear transformation (`linear`). Its dimension should be `20` x `7`.

