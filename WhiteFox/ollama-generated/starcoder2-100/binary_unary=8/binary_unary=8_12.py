
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor 
        v3  = F.relu(v2) # Apply ReLU to the result
        return v3

# Initializing model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Initialize another tensor
other_tensor = torch.randn(1, 8, 20, 20).requires_grad_() 

__output__  = m(x1), other_tensor

