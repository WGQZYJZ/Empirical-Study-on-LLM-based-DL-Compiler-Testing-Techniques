
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, scale_factor=None):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return output
 
class Model_2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_1 = torch.nn.MultiheadAttention()
        self.attention_2 = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, scale_factor=None):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = self.attention_1(softmax_qk, value) # Compute the output of the first attention layer using the dropout of the second attention layer
        return output
