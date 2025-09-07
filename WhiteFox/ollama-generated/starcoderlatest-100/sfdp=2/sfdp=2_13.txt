
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2):
        qk = self.attention_layer(x1, x2)[0] # The attention layer computes query and key vectors first
        scaled_qk = qk.div(inv_scale_factor) # Then scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Finally apply softmax to get the final attention scores
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Finally compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # A batch of queries
x2 = torch.randn(1, 8, 64, 64) # A batch of keys


