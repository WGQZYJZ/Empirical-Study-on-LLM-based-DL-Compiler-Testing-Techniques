
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
         v0 = self.conv(x).reshape(-1)
         v1 = (v0 - 0.75 * torch.ones_like(v0)) # Subtract a constant tensor from the output of the convolution
         v2 = torch.relu(v1)
         return v2


# Initializing the model and its weights, including bias for ReLU activation function.
m  = Model()
torch.nn.init.zeros_(m.conv.bias) # Initializes all elements of weight bias in the model Conv2d to zero. 

