
class Model(torch.nn.Module):
    def __init__(self, num_queries, query_dim, d_model):
        super().__init__()

        self.num_queries = num_queries
        self.query_dim = query_dim
        self.d_model = d_model

        # The dot product of the query and the key for each element in batch
        qk = torch.nn.Linear(self.query_dim * 2, 8)

        self.attention_probs = torch.nn.Softmax(dim=-1)

    def forward(self, x):
        # Compute the dot product of the query and the key for each element in batch
        qk = torch.matmul(x, self.q_proj).reshape(-1, 8 * self.num_queries)

        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)

        # Compute the attention probabilities for each element in batch
        attention_probs = self.attention_probs(dropout_qk).reshape(-1, 8 * self.num_queries)

        # Combine the attention output from all elements in a single tensor
        v = (attention_probs * dropout_qk.unsqueeze(dim=0)).sum(dim=-2)
        return v


# Initializing the model
m = Model(4, 16, 32)

# Inputs to the model
x = torch.randn(1, 4, 8)
