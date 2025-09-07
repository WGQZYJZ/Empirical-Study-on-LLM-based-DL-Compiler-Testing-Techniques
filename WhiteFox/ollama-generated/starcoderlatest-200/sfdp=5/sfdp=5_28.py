
class Attention_1d_Dot_Product(torch.nn.Module):
    def __init__(self, d_key: int = 64, d_value: int = 256) -> None:
        super().__init__()
        self._attention_dropout = torch.nn.Dropout(p=0.1)
        self._q_dense = torch.nn.Linear(d_model * 3, d_key * 4)
        self._k_dense = torch.nn.Linear(d_model * 3, d_value * 2)
 
    def forward(self, x: torch.Tensor):
        query, key, value = torch.chunk(x, 3, dim=1)
 
        qk  = self._q_dense(torch.cat([query, key], dim=1)) # Compute the dot product of the query and key
        qk = self._attention_dropout(qk) # Add dropout to qk
        attn_weights = torch.softmax(qk, dim=-1) # Apply softmax to the scaled dot product

        attn_weights = self._attention_dropout(attn_weights) # Add dropout to attn_weight
 
        output  = (attn_weights @ value).transpose(1, 2) # Compute the dot product of the attention weights and the value
        output = torch.cat([output, query, key], dim=1) # Concatenate the output with input and key
        return output


# Initializing the model
model = Attention_1d_Dot_Product()


# Inputs to the model
x = torch.randn(4, 3, 64, 64)
