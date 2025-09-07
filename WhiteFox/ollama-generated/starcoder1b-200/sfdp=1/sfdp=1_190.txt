
class Model(torch.nn.Module):
    def __init__(self, dim_input, dim_head, num_attention_heads=4):
        super().__init__()
        self.dim_input = dim_input
        self.dim_head = dim_head
        self.num_attention_heads = num_attention_heads
 
        self.qkv = torch.nn.Linear(dim_input, dim_head * 3)  # qkv is the same as query-key vector, q is a batch size vector, k is a sequence length vector and v is an unnormalized key vector.
        self.scale_factor = (dim_head ** -0.5)
 
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, x):
        bsz, seqlen, dim_input = x.shape
        qkv  = self.qkv(x).reshape(bsz * seqlen, -1, self.num_attention_heads, self.dim_head)  # Get the qkv for each token in the batch
        k = qkv[:, :, :, 0].contiguous().view(-1, seqlen, dim_input)
        v = qkv[:, :, :, 1].contiguous().view(-1, seqlen, dim_input)
        k  *= self.scale_factor # Set k to the scale factor
        scaled_k = k.matmul(self.scale_factor)  # Compute the dot product of the input with itself
        qkv /= self.scale_factor  # Scale the dot product by the inverse scale factor
        attention  = torch.matmul(qkv, scaled_k.transpose(-2, -1)) # Compute the dot product of the qkv and key tensors, then transpose the result to convert to the original shape
        attention = self.softmax(attention) # Apply softmax to the attention values
        output = torch.matmul(attention, v)  # Apply the dot product with the value tensor
        return output


# Initializing the model
m = Model(dim_input=128, dim_head=64, num_attention_heads=16)

