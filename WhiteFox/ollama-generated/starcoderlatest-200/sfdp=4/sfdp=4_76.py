
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_conv1 = torch.nn.Conv2d(8, 8, 3, stride=1) # Convolution with kernel size 3 and stride of 1 for the output dimension to be 8 
        self.attn_conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0) # Convolution with kernel size 1, stride of 1, and padding of 0
        self.value_conv = torch.nn.Conv2d(16, 32, 1, stride=1, padding=0)

    def forward(self, query):
        attn_feature = self.attn_conv1(query) # Apply convolution to get the attention features for each key 
        attn_feature = torch.relu(attn_feature)
        attn_feature = self.attn_conv2(attn_feature) # Apply convolution to obtain the scaled dot product

        value_feature = self.value_conv(query) # Compute values for the keys, and reshape them as a feature map with channels equal to the number of keys
        value_feature = torch.reshape(value_feature, (1, 32, -1))

        v2  = torch.matmul(attn_feature, value_feature)
        return v2 # Return the output tensor


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 8, 64, 64)
k1 = torch.randn(2, 8, 64, 64)
