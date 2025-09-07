
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim_model=512, num_heads=4):
        super().__init__()
        self.dim_model = dim_model
        self.num_heads = num_heads
        self.dropout = torch.nn.Dropout(p=0.0)
        self.head_dim = dim_model // num_heads

        # Create the two linear layers
        self.key_layer = torch.nn.Linear(self.dim_model, self.num_heads * self.head_dim)
        self.value_layer = torch.nn.Linear(self.dim_model, self.num_heads * self.head_dim)

        # Create the two fully connected layers (linear in-place transformation of shape dim_model -> num_heads*head_dim and linear for output transformation with shape num_heads*head_dim->dim_model)
        self.attention_score = torch.nn.Linear(self.num_heads * self.head_dim, 1, bias=False) # Bias is not used as it is assumed to be zero during evaluation

    def forward(self, x1):
        # Compute the query, key and value
        qk = torch.matmul(x1, self.key_layer.weight)

        # Apply dropout
        qk = self.dropout(qk)

        # Compute the attention scores based on the dot product of the two vectors (attention score)
        attn_score = self.attention_score(qk)

        # Compute the softmax values for each of the heads to determine the weights of each head in the output vector
        softmax_attn_score = torch.nn.functional.softmax(attn_score, dim=-1) # Apply softmax to attention scores

        # Dropout is applied during training phase
        if self.training:
            softmax_attn_score = self.dropout(softmax_attn_score)

        # Compute the output vector based on the scaled dot product of the values for each head and their respective weights (attention weighted value). We can then concat the vectors as we have one attention head per output dimension
        x1 = torch.matmul(softmax_attn_score, self.value_layer.weight)

        return x1


# Initializing the model
m = MultiHeadAttention()

# Inputs to the model
x1 = torch.randn(32, 512, 64, 64) # The shape of the inputs is different in each case
