
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, value_dim, embed_dim, num_heads=8, num_layers=1, p=0.025):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embed_dim)  # Embedding layer to obtain a representation for each token
        self.scale_factor = torch.sqrt(embed_dim)
        self.query = torch.nn.Linear(query_dim + key_dim, embed_dim * num_heads, bias=True)  # Linear layers for the query and keys
        self.value = torch.nn.Linear(value_dim, embed_dim * num_heads, bias=True)  # Linear layers for the query and keys
        self.num_layers = num_layers  # Number of transformer layers
        self.p = p  # Dropout probability

    def forward(self, x1):
        q = self.query(torch.cat((x1[:, None], x1), dim=-2)).view(batch_size * (max_len - 1), embed_dim)  # Query for the last layer
        k = self.value(x1)  # Key and value for each head

        scaled_qk = q.bmm(k.transpose(-2, -1))  # Compute dot product of the query and key tensors
        softmax_qk = F.softmax(scaled_qk.mul(self.scale_factor).exp(), dim=-1)  # Apply softmax to the dot product
        dropout_qk = F.dropout(softmax_qk, p=self.p, training=True)  # Dropout applied on the output of softmax layer
        x2 = dropout_qk.matmul(x1)  # Compute dot product of the query and key tensors with the value

        return x2


# Initializing the model
m = Model()

