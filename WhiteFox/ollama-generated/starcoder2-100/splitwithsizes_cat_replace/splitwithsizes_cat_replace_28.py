
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return torch.split(x1, 32)[0].size() # Split the input tensor into three tensors of size 64 * 8 using `torch.split`, and return the first split tensor's size

# Initializing the model
m = Model()
 
# Inputs to the model
input_tensor  = torch.randn(32, 100)
 
__output__  = m(input_tensor)

