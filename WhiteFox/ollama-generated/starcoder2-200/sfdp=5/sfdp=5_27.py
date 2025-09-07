
class MultiHeadAttentionModel(torch.nn.Module):
    def __init__(self, d_model: int=512) -> None:
        super().__init__()
        self.d_model = d_model
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        attn  = qk @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key
        attn  = attn + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(attn, dim=-1)  # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing model
m1=MultiHeadAttentionModel()
 
# Inputs for the model.
query1 = torch.randn(2, 8, 512)
key1 = torch.randn(2, 8, 512)
value1 = torch.randn(2, 8, 512)
__output1__=m1(query1, key1, value1)

