
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scaled_key):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / inv_scale_factor  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention()
 
    def forward(self, query, key, value):
        attn_output = self.attention(query, key, value, scaled_key)  # Apply the attention mechanism to query, key and value tensor
        return attn_output


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 32, 56, 56)
k1 = torch.randn(1, 128, 16, 16)
v1 = torch.randn(1, 256, 48, 48)


# Input tensors to the model
