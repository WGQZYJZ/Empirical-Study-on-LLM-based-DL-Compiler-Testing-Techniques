
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        self.attn = torch.nn.MultiheadAttention(input2)
        v1  = input1 @ (input2.transpose(-2, -1)) / math.sqrt(input2.size(-1))
        v2  = v1 + input1[:, None] # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1)
        v4  = v3 @ input1
        return v4


# Initializing the model
m  = Model()

# Inputs for the model:
i1  = torch.randn(8, 56, 768).cuda() # Query of size [8 x 56 x 768]
i2  = torch.randn(8, 56, 768).cuda() # Key and Value tensors with the same shape

 __output__  = m(i1, i2)
