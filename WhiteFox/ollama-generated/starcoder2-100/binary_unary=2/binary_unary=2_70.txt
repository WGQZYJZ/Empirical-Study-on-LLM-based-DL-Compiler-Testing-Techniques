
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
      v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
      v2 = v1 - other # Subtract a tensor or scalar "other" from the output of the convolution
      v3 = torch.relu(v2) # Apply ReLU (Rectified Linear Unit) activation function to the result
      return v3


# Initializing the model and setting values for "other" 
m  = Model()
other  = other_tensor # Setting a constant tensor for "other". The initial value of other is 0.5, but you need to set it as another tensor with random values such as torch.randn(1) so that it changes at each call.


# Inputs to the model
x1  = torch.randn(1,3,64,64) # The input is of size [N,C,H,W] (where N is batch dimension). It must be in a random state with every call of your script but you can use any fixed input tensor. We will set the batch size as 1.
