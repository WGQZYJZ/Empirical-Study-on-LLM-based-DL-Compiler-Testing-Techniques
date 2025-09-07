
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v0  = x1.view(-1, 3 * 64 * 64).to(torch.device('cuda')) # Reshape the input tensor to a 2D matrix with shape [batch_size, channel * height * width]
        v1  = self.linear(v0) # Apply a linear transformation to the reshaped input tensor
        v2  = torch.nn.functional.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        v3  = v1  * v2 
        return v3


# Initializing the model