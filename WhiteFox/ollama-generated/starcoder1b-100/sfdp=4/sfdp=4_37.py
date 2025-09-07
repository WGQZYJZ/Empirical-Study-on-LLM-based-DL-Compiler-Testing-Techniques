
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(512, 512)
        self.key    = torch.nn.Linear(512, 512)
        self.value  = torch.nn.Linear(512, 512)
 
    def forward(self, x):
        # Compute the scaled dot-product of the input and each embedding vector (in this case: 3072).
        query_dot_product  = x @ self.query
        # Scale it by dividing by sqrt(embedding dimension).
        scaled_query_dot_product  = query_dot_product / torch.sqrt(self.key.weight.size(-1))
        key_dot_product        = self.key @ self.key
        # The softmax will normalize the input so that it sums to one per example (otherwise, each row and column would have a very small value)
        attn_weights          = torch.softmax(scaled_query_dot_product @ key_dot_product, dim=-1)
        # Compute the dot product between scaled_query_dot_product and the embeddings of the input.
        query_value  = self.value @ attn_weights  # (batch_size x 512) * (embedding_dim x 3072) = (batch_size x 512) x (embedding_dim x 3072) => (batch_size x 512) x (embedding_dim x 3072)
        # Sum the values of this dot product, divided by sqrt(embedding_dim), and use them as the result of the output layer.
        attn_output = query_value / torch.sqrt(self.value.weight.size(-1))
        return attn_output


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(32, 512, 7, 7)
