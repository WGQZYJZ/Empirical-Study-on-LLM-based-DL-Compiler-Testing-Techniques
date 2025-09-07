
class Transformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential()
        for _ in range(2):
            self.layers += nn.Sequential(
                nn.Linear(10, 10),
                nn.ReLU(),
                nn.Dropout(0.5)
            )

    def forward(self, query, key, value):
        attn_mask = torch.full((query.size(-2), key.size(-2)), -float('inf'), dtype=torch.float32).to(query.device)
        qk  = (query @ key.transpose(-1, -2)) / math.sqrt(query.size(-1)) + attn_mask # Compute the dot product of the query and key tensors, and scale it by dividing each element by sqrt(query_length)
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the scaled dot-product result
        output  = (attn_weight @ value).type(torch.float32) * math.sqrt(query.size(-1)) # Compute a weighted sum of the value tensor and multiply it by sqrt(query_length), which is equivalent to applying layer normalization to the original query

# Initializing the model
m  = Transformer()


# Inputs for the model:

qk   = torch.randn([2,4096,1538]) + (query @ key.transpose(-1, -2)) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key tensors, and scale it by dividing each element by sqrt(query_length)

attn_mask = torch.full((query.size(-2), key.size(-2)), -float('inf'), dtype=torch.float32).to(query.device)

qk  += attn_mask # Add the attention mask to the scaled dot-product result


attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the scaled dot-product result

output   = (attn_weight @ value).type(torch.float32) * math.sqrt(query.size(-1)) # Compute a weighted sum of the value tensor and multiply it by sqrt(query_length), which is equivalent to applying layer normalization to the original query

