
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(8, 2)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = self.attention_layer(query, key, value,
                                    attention_mask=None)[0]
        return output


# Initializing the model
m = Model()


