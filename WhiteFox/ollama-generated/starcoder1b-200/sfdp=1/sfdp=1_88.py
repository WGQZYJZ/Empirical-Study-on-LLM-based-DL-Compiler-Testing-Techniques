
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(1, 4, 1)  # Convolution to the input tensor for the first layer
        self.key_conv   = torch.nn.Conv2d(4, 8, 1)  # Convolution to the value tensor for the second layer
        self.value_conv = torch.nn.Conv2d(8, 32, 1)  # Convolution to the query tensor for the third layer
 
    def forward(self, x1):
        q  = self.query_conv(x1)   # Compute the first layer
        k  = self.key_conv(x1)     # Compute the second layer
        v  = self.value_conv(q)    # Compute the third layer
        return torch.nn.functional.linear(q, v)  # Apply linear to the dot product of the two tensors
 

# Initializing the model
m = Model()


