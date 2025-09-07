
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        v1  = torch.nn.functional.conv2d(input, self.linear1)
        v10= torch.nn.functional.batch_norm(v1, running_mean, running_var)
        v4 = torch.nn.functional.conv2d(self.linear1, self.linear3, 6) 
        return v1+v10

# Initializing the model
m  = Model()

# Inputs to the model: 
input  = torch.randn(5,4,8,8)

 # Running inference with the original forward pass
__output__= m(input) 

 