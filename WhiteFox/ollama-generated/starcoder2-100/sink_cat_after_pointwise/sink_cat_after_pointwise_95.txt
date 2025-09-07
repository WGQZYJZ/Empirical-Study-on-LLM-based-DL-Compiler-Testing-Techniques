
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v2  = torch.nn.functional.linear(x1[:,0:3], self.linear.weight[None,:])  # Apply linear transformation to the first 3 columns of the input tensor.
       v1  = v2 + self.linear(x1[:,0:2]) 
       return v1

# Initializing the model
m  = Model()

