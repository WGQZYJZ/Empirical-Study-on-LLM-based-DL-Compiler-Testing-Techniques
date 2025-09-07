
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        q = self.linear(x1)
        k = self.linear(x2)
        v = self.linear(torch.randn_like(k))
        q = q / math.sqrt(q.size(-1))  # Normalize the query, because the model is trained on a log scale and this is also how other models work (e.g., BERT, RoBERTa)
        k = k / math.sqrt(k.size(-1))
        v = v / math.sqrt(v.size(-1))
        output  = torch.matmul(q, k)  # Compute the dot product of the query and key
        attention_weights  = torch.softmax(output, dim=-1)  # Apply softmax to the result
        weighted_sum  = torch.matmul(attention_weights, v)  # Compute the weighted sum of the value tensor
        return weighted_sum


# Initializing the model
m = Model()


