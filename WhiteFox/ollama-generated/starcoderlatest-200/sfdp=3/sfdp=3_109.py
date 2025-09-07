
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_attention_heads=8, num_key_value_projections=4):
        super().__init__()
        self.num_attention_heads = num_attention_heads
        self.num_key_value_projections = num_key_value_projections
 
        self.qkv  = torch.nn.Sequential(
            torch.nn.Linear(128, num_attention_heads * (3*4)),
            torch.nn.GELU(),
            torch.nn.Linear(num_attention_heads * (3*4), num_key_value_projections)
        )
 
    def forward(self, x):
        q, k, v = self.qkv(x).split([128], dim=-1)
        q, k, v = [q, k, v].permute(0, 3, 4, 2, 1)
        qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v) # Compute the dot product of the dropout output and the value tensor
        return qk


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
