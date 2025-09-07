
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)  # A linear transformation from query to key
        self.key = torch.nn.Linear(d_model, d_k)  # A linear transformation from key to value
        self.value = torch.nn.Linear(d_model, d_v)  # A linear transformation from value to output

    def forward(self, x):
        # Compute dot product of query and key
        qk = torch.matmul(x, self.key.weight)
        # Scale dot product by inverse of scaling factor
        scaled_qk = qk / math.sqrt(float(d_k))  # Scaled query key pair
        # Softmax over the scaled dot product to obtain attention weights
        attn_weights = F.softmax(scaled_qk, dim=-1)
        # Dropout can be used to prevent the attention model from considering a particular token if all tokens in a sequence have zero attention scores
        attn_output = dropout(attn_weights, p=dropout_p)  # Output of the softmax layer before applying dropout
        # Compute dot product of output and value
        v = torch.matmul(attn_output, self.value.weight)  # Dot product between output and value
        # Apply dropout to the resulting dot product
        v = dropout(v, p=dropout_p)  # Dropout over the attention weights
        return v


# Initializing the model
m = Model()


