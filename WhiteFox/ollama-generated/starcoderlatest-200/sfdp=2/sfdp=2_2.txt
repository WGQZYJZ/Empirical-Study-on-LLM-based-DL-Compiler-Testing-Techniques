
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value):
        vq  = self.conv(query) # Compute the output of a convolution layer with kernel size 1 and stride 1, padding 1 and input x1
        dk  = torch.nn.functional.conv2d(key, -vq.detach(), bias=None, stride=(1, 1), groups=8) # Compute the output of a convolution layer with kernel size 1 and stride 1, padding 1 and input -vq, and then negate the result
        dk = dk * dk  # Compute the output of the element-wise product of vq and dk
        dk = dk.softmax(dim=-1)
        vdk = dk.matmul(value)
        vdk = self.conv(vdk)
        return vdk
 


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, 64, 64) # Input of size (bs, n_heads, sl, d_k), where bs is batch_size, sl is sequence length, and d_k is dimension of each head
        key   = torch.randn(1, 3, 64, 64) # Input of size (bs, n_heads, sl, d_k)
        value = torch.randn(1, 3, 64, 64) # Input of size (bs, n_heads, sl, d_v)
