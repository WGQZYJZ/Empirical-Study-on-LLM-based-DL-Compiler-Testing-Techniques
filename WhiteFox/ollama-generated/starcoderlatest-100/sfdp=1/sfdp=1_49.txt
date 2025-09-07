
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 3)
 
    def forward(self, x1, x2):
        query = torch.nn.functional.linear(x1, self.project_q, bias=self.bias) # Project the key to a different dimension
        query = query.transpose(-2, -1) # Transpose for broadcasting with the value and scaled dot product
        key = torch.nn.functional.linear(x2, self.project_k, bias=self.bias) # Project the value to a different dimension
        key = key.transpose(-2, -1)
        qk = self.attention(query, key, key)[0] # Compute and apply multihead attention to obtain attention weights on all locations
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.output_layer(torch.matmul(dropout_qk, self.attn_v)) # Compute and apply matrix multiplication
        return output
 
    def forward(self, x1):
        query = torch.nn.functional.linear(x1, self.project_q, bias=self.bias) # Project the key to a different dimension
        query = query.transpose(-2, -1) # Transpose for broadcasting with the value and scaled dot product
        key = x2 # Use the same keys as the values
        qk = self.attention(query, key, key)[0] # Compute and apply multihead attention to obtain attention weights on all locations
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.output_layer(torch.matmul(dropout_qk, self.attn_v)) # Compute and apply matrix multiplication
        return output
 

# Initializing the model
m = Model()
 
