
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        vv = vq * (inv_scale_factor / torch.pow(key_scale_factor, math.sqrt(math.prod(value_scale_factors))))  # Scale the dot product by the inverse scale factor
        vr = vq.softmax(-1) # Apply softmax to the scaled dot product
        vr = dropout_v * vr  # Apply dropout to the softmax output
        vv = dropout_v * vv # Compute the dot product of the dropout output and the value tensor
        return vv + x2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(8, 32, 100, 100)
