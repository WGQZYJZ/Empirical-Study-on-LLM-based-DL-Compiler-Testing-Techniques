
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1  = torch.nn.functional.linear(x1) # Applying a linear transformation to the input tensor 
        l2 = self.__add__(l1,3) # Adding 3 to the output of the linear transformation  
        l4 = torch.clamp_min(l2,0) # Clamping the output of the addition operation to a minimum of 0
        l5 = torch.clamp_max(l4,6)# Clamping the output of the previous operation to a maximum of 6 
        l7 = torch.__truediv__(l5,3) # Dividing the output of the previous operation by 3
        return l7


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2048, dtype=torch.float64)# The input tensor is of size 2048
