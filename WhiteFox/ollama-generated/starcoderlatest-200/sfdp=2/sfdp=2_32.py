
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=512, hidden_dim=512):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.linear = torch.nn.Linear(embedding_dim, hidden_dim)
        self.attn_layer = AttentionLayer()
 
    def forward(self, x):
        # Linear layer to the input tensor
        embedded_x = self.embedding(x)
        linear_out = self.linear(embedded_x)
        # The output of linear layer is now used as the input for attention computation
        # This function computes the output and attn_weights
        # It returns a tuple containing:
        # 1) A tensor named "output" representing the final output
        # 2) A variable named "attn_weights" representing the weights assigned to each attention head
        return self.attn_layer(linear_out, linear_out, linear_out), None
 

class AttentionLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, attn_mask=None, dropout_p=0.1):
        # Apply the dot product between query and key to compute attention weights
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(np.sqrt(embedding_dim))

        # Scale the dot product by sqrt(embedding_dim)
        attn_weights = softmax(scaled_qk, dim=-1)

        if dropout_p > 0:
            # Apply dropout to the attention weights (scaled dot product values),
            # and then sum them up for further computation.
            dropout_attn_weights = torch.nn.functional.dropout(
                attn_weights, p=dropout_p)

            # Addition between scaled and dropout attention weights
            output = (dropout_attn_weights * v).sum(dim=-2)
        else:
            # Just take the product of scaled dot product values with value tensor.
            # This is the final step in computing the attention scores.
            output = (attn_weights * v).sum(dim=-2)

        return output, attn_weights
 


# Initializing the model
m = Model()
x  = torch.randn((10, 3))
__output__, __attn_weights__ = m(x)


