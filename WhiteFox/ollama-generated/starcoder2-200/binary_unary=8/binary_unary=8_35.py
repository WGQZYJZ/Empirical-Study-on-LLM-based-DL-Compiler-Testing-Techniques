
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8,8, 3, stride=1, padding=1)

    def forward(self, x): 
        t0 = self.conv1(x).clone() # Apply pointwise convolution with kernel size 3 to the input tensor
        t1 = self._ops(t0, other_tensor, op="add") + other  # Add another tensor to the result of the convolution
        t2 = torch.relu(t1)  # Apply the ReLU activation function to the result of the convolution and add operation
        t3 = self.conv2(t2).clone() 
        return [t0, t1, t2, t3]
 
# Initializing the model
m = Model().to('cuda')

