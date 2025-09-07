
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_qkv = torch.nn.Linear(4096, 3072)
 
    def forward(self, qk):
        v1 = torch.matmul(qk[0], k[1].transpose(-2, -1)) # Compute the dot product of query tensor and key tensor
        scaled_v1 = v1.mul(scale_factor)
        softmax_v1 = scaled_v1.softmax(dim=-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        output = dropout_v1.matmul(v2) # Compute the dot product of dropout tensor and value tensor
 
        return output


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(4096, key_channels, key_height, key_width)  # Input query tensors in shape (batch, heads, height, width)
k = torch.randn(3072, key_channels, key_height, key_width)  # Input key tensors in shape (batch, heads, height, width)
v = torch.randn(4096, value_channels, value_height, value_width)  # Input value tensors in shape (batch, heads, height, width)
 
