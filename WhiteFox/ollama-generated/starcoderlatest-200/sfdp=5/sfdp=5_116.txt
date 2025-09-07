
class Model(torch.nn.Module):
    def __init__(self, num_heads=128):
        super().__init__()
 
        # This block defines the input tensor which is passed to the transformer block
        self.conv  = torch.nn.Conv2d(3, 64, kernel_size=(1, 1))
        # The first three convolutions here are identical to the previous one except for changing out kernel size and number of channels from 1024 to 64, since we only need a single feature map from these 6 layers on top, so the remaining three layers can be skipped. Then this is followed by two transformer blocks
        self.conv_1 = torch.nn.Conv2d(64, 64, kernel_size=3, stride=(2, 1), padding=0)
        self.conv_2 = torch.nn.Conv2d(64, 64, kernel_size=5, stride=(2, 1), padding=2)
        # The transformer blocks are then defined as follows: a multihead attention block is added between two adjacent layers, followed by another convolutional layer that reduces the number of channels to half. After all these transformer blocks, we add a residual connection and a batchnorm layer before applying linear transformation on the input tensor again in order to bring it up to full resolution.
        self.attn_block = torch.nn.ModuleList([
            ResidualBlock(conv=Conv2DWrapper(), pool=AvgPool2DWrapper()), 
            TransformerBlock(num_heads=num_heads),
            ResidualBlock(conv=Conv2DWrapper())])
        
        # This is a linear transformation on the input tensor after applying all these transformer blocks and then one more convolutional layer to bring it up to full resolution
        self.linear = torch.nn.Linear(196, 4096)
    
    def forward(self, x1):
 
        v1 = self.conv(x1) # This is the output of the first convolution
        # The second three layers are identical to the third and forth ones except that we skip them. They also need to be skipped because their outputs will just be the identity matrix for each point in the input tensor.
        x2 = v1
        x3 = self.conv_2(self.conv_1(x2))
        # Then this is followed by two transformer blocks defined as above with 64 heads and the output of the last convolution layer being used as input to the linear transformation block here
        out = self.attn_block[0](self.attn_block[1](self.attn_block[2](x3)))
 
        # Finally this is followed by one more linear transformation on the resulting tensor and then a linear transformation from that output for a final classifier layer
        return F.linear(out, self.linear.weight, self.linear.bias)
 

# Initializing the model with 64 heads
m = Model(num_heads=64)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
