
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = other + self.conv(x1) # A ReLU activation function would also not be in the code
        return torch.relu(v0)
 
# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
other = torch.zeros((1,8,64,64), requires_grad=True) # other would be added to the output of conv
 
 # Initializing a Tensor to be added
other.data.normal_(0, 1e-25) 
 
__output__  = m(input_tensor)

