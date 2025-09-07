
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=16, num_heads=8)
 
    def forward(self, qk1, vk1, sk1):
        qk  = torch.matmul(qk1, sk1.transpose(-2, -1)) # Compute the dot product of query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(vk1) # Compute the dot product of the dropout output and value tensor
        return output


# Initializing the model
m = Model()

