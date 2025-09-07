
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.ops.tensorpipe.matmul_op
 
    def forward(self, x1, x2, x3, x4):
        v1  = self.mm(x1, x2)
        v2  = self.mm(x3, x4)
        v3  = v1 + v2 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(70, 50) # Matrix multiplied with input_tensor 1
x2  = torch.randn(50, 60) # Matrix multiplied with input_tensor 2 
x3  = torch.randn(40, 90) # Matrix multiplied with input_tensor 3 
x4  = torch.randn(90, 70) # Matrix multiplied with input_tensor 4


__output__  = m(x1, x2, x3, x4)

