
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1).contiguous() # Make a view of the input tensor
        qk = torch.matmul(v1, x2.transpose(-2, -1)) # Compute the dot product of both inputs
        s  = torch.softmax(qk)  # Apply softmax to the dot product
        v3 = s.mul(x2).contiguous() # Scale the dot product by the inverse sqrt of the value tensor, and apply dropout on the result
        v4 = s.mul(1.0 - x2).contiguous()
        output = v3 * v4  # Compute the dot product of the input tensor with the scaled and softmax output
        return output


# Initializing the model
m = Model()


