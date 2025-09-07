
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.fc    = torch.nn.Linear(64*5, 8)
 
    def forward(self, x1): 
        v1  = self.conv(x1)  # Apply pointwise convolution to the input tensor with kernel size 1 and stride 2, then add zeros as necessary to match the output of the convolution
        v1_reshaped  = torch.flatten(v1, start_dim=0).view(-1, 64*5) 
        v2 = self.fc(v1_reshaped) # Apply pointwise linear transformation to the output of the convolution
        v3  = v2 * 0.5 # Multiply the output of the linear transformation by 0.5
        v4  = v2 * 0.7071067811865476 # Multiply the output of the linear transformation by 0.7071067811865476
        v5  = torch.erf(v4) # Apply the error function to the output of the linear transformation 
        v6  = v3 + v5 # Add the output of the linear transformation and its error function
        return v2
 

# Initializing model
m = Model()

 # Inputs to model 
 x1   = torch.randn(1, 3, 64, 70)
  