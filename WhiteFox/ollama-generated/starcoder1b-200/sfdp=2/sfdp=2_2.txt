
class Model(torch.nn.Module):
    def __init__(self,
                 num_heads=1,  # Number of heads to use for the Multi-head Attention module
                 dim_key=64,  # Size of key vector
                 dropout_p=0.15):  # Dropout probability for Multi-head Attention
        super().__init__()
 
        self.mha = torch.nn.MultiheadAttention(
            num_heads=num_heads,
            dim_key=dim_key,
            dropout=dropout_p)
 
    def forward(self, x1, x2):
        scaled_x1, inv_scale_factor = mha_core.split_heads(mha=self.mha, x1=x1, num_heads=num_heads)  # Split the heads of the input tensor into the multiple heads to attend on the different dimensions in the feature map
        scaled_x2, _ = mha_core.split_heads(mha=self.mha, x2=x2, num_heads=num_heads)
        output = torch.cat([scaled_x1 * inv_scale_factor, scaled_x2], dim=-1)  # Compute the dot product of the two heads
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 64, 64, 3)  # Generate a 4-element input tensor
