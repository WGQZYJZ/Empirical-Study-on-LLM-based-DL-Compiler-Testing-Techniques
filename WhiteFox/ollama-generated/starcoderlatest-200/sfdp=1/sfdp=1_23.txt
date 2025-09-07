
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads: int = 256):
        super().__init__()
        self.attention_heads = torch.nn.Linear(3 * 108, num_attention_heads)
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v2  = (query + key).view(3 * 2048, -1) # Perform addition and rearrange tensor
        qk  = self.attention_heads(v2) # Compute the attention heads using linear transformation
        scaled_qk = qk.div(self.inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
# Inputs to the model
query  = torch.randn(1, 3 * 2048, 64, 64)
key    = torch.randn(1, 3 * 2048, 64, 64)
value  = torch.randn(1, 3 * 108, 64, 64)
