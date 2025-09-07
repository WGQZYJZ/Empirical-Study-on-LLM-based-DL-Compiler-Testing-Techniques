
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + self._other_tensor() # Adding another tensor here is allowed, because the model passes an argument as a keyword argument in the forward function definition
        v3  = torch.nn.functional.relu(v2) 
        return v3

# Initializing the model
m  = Model().cuda()


# Inputs to the model
x1  = torch.randn(8, 10).cuda() # Input tensor on GPU
__output__  = m._other_tensor() # This argument is provided as a keyword argument and should be added to the output of another function
__output__2 = m(x1)

