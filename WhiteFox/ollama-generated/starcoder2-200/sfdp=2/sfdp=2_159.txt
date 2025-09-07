
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        v2  = v1 / math.sqrt(num_attention_heads) # Scale the dot product by sqrt(number of attention heads)
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output
        return v4.matmul(value)


# Initializing model<|end_of_model|>
m = Model()


# Input to the model<|end_of_input|>
q  = torch.randn(2, 8, 64) # The query tensor of size [2, num_attention_heads * number_of_key_words]
k = q.clone() # Copy and reuse this key
v = k.clone()


__output__= m(q, k, v)<|end_of_model|>
