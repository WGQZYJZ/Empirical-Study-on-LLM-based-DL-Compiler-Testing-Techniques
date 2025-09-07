
class Model(torch.nn.Module):
    def __init__(self, num_attention=None, hidden_size=512):
        super().__init__()
        self.num_attention = num_attention if isinstance(num_attention, int) else None
        self.hidden_size = hidden_size
 
    def forward(self, input, key, value, attn_mask):
        batch_size, seq_length, input_dim  = input.shape
        assert hidden_size % self.num_attention == 0
        head = (hidden_size // self.num_attention) * self.num_attention
        if self.num_attention is None:
            query = torch.bmm(input, key) / math.sqrt(head)
        else:
            num_heads = self.num_attention
            query = torch.matmul(
                input, key.transpose(-2, -1)
            ) / math.sqrt(head * num_heads)

        if attn_mask is not None:
            attn_weight = torch.softmax(query, dim=-1)  # Apply softmax to the result
            value = attn_weight @ value  # Compute the dot product of the attention weights and the value
        else:
            attn_weight = torch.softmax(query, dim=-1).unsqueeze(-2).repeat(1, seq_length, 1)

        return value


# Initializing the model
m = Model()


