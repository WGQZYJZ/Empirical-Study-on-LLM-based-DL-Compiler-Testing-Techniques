
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(16, 128)
        self.linear_k = torch.nn.Linear(16, 128)
        self.linear_v = torch.nn.Linear(16, 128)
 
    def forward(self, q1, k1, v1):
        # Compute the attention mechanism
        scaled_q1 = self.linear_q(q1).unsqueeze(-3).unsqueeze(-2)
        scaled_k1 = self.linear_k(k1).unsqueeze(-3).unsqueeze(-2)
        scaled_v1 = self.linear_v(v1)

        q1 = scaled_q1 * 0.5 # Scale the query tensor by 0.5
        k1 = scaled_k1 * 0.5 # Scale the key tensor by 0.5
        v1 = scaled_v1 * 0.7071067811865476 # Scale the value tensor by 0.7071067811865476

        dot_product = torch.matmul(q1, k1.transpose(-2, -1)) # Apply pointwise convolution
        softmax_dot_product = dot_product / math.sqrt(self.linear_v.in_features) # Compute the softmax of the dot product
        softmax_dot_product = torch.nn.functional.softmax(softmax_dot_product, dim=-1) # Apply softmax to the output of pointwise convolution
        dropout_dot_product = torch.nn.functional.dropout(softmax_dot_product, p=dropout_p) # Apply dropout to the softmax output

        attention_weights = dropout_dot_product.matmul(v1).squeeze(-3).squeeze(-2) # Compute the dot product of the attention weights and the value tensor
        attention_weights /= math.sqrt(self.linear_v.in_features) # Normalize the attention weights to have unit norm

        return attention_weights


# Initializing the model
m = Attention()


# Inputs to the model
query  = torch.randn(3, 16)
key    = torch.randn(4, 16)
value  = torch.randn(5, 16)
