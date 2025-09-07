
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attention = torch.nn.Linear(128, 512)
        self.output_layer = torch.nn.Sequential(
            torch.nn.Linear(2048, 6), # Output the scores of all classes in one line. The first column represents the confidence of the image being a "0". And so on. 
            torch.nn.Softmax()
        )
 
    def forward(self, q1, k1, v1):
 
        self_attention = self.attention(q1) # Apply linear transformation to the query tensor
        attention = torch.matmul(k1, self_attention)  # Compute the dot product between the key tensor and the self-attention output of the query tensor.

        # Scale the dot product by the inverse scale factor
        scaled_attention = attention / (scale_factor**0.5)
 
        # Apply softmax to the scaled dot product
        softmax_attention = torch.nn.functional.softmax(scaled_attention, dim=-1)
 
        # Apply dropout to the softmax output
        dropout_attention = torch.nn.functional.dropout(softmax_attention, p=dropout_p)

        context_vector = torch.matmul(v1, dropout_attention)  # Compute the dot product between the value tensor and the attention output of the key tensor multiplied by the output from softmax applied to scaled dot product
        output = self.output_layer(torch.cat((context_vector, q1), dim=1))

        return output

# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(1, 256) # Query tensor: (batch_size, embedding_dim)
k1 = torch.randn(3, 256) # Key tensor: (num_keys, embedding_dim). In this case, we have three classes in the classification task. We use "0", "1", and "2". So there are three keys in total, which is different from the number of keys in the previous pattern that we used for generating the dot product matrix.
v1 = torch.randn(3, 512) # Value tensor: (num_values, embedding_dim). In this case, we have three classes in the classification task. We use "0", "1", and "2". So there are three values in total, which is different from the number of keys in the previous pattern that we used for generating the dot product matrix.
