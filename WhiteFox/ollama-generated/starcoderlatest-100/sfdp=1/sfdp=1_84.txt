
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = self.dropout(softmax_qk) # Apply dropout to the softmax output
        return (dropout_qk.matmul(value))
 
 class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.attention = Attention()
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) # Apply convolution with kernel size (3, 3), stride 1, and no padding to the input tensor
        v2 = self.attention(v1, x2, key=x2) # Compute attention on the output of the first convolutional layer and x2
        return v2
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
x2 = torch.randn(256, 3, 64, 64)
