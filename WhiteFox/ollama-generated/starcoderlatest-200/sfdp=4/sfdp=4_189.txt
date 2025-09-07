
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Conv2d(8, 64, kernel_size=1) # Conv layer for the query with dimension 8 (input size of the convolution is equal to the number of output units), kernel size of 1x1 and stride of 1 
        self.attn_k = torch.nn.Conv2d(8, 64, kernel_size=1) # Conv layer for the key with dimension 8 (input size of the convolution is equal to the number of output units), kernel size of 1x1 and stride of 1
        self.attn_v = torch.nn.Conv2d(8, 64, kernel_size=1) # Conv layer for the value with dimension 8 (input size of the convolution is equal to the number of output units), kernel size of 1x1 and stride of 1
 
    def forward(self, q):
        q = self.attn_q(q)
        k = self.attn_k(q)
        v = self.attn_v(q)

        d_k = torch.sqrt(k.size(-1)) # Compute dimension-wise squared Euclidean norm for key tensor
        attn_weights  = torch.softmax(q @ (k.transpose(-2, -1)) / d_k, dim=-1)
        output        = attn_weights @ v
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(32, 8, 64, 64) # Query tensor with dimension of 32x8x64x64 
key = torch.randn(1024, 8, 64, 64) # Key tensor with dimension of 1024x8x64x64 

