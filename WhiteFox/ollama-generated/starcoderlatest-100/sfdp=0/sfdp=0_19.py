
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads=8, dropout=0.1):
        super().__init__()
        self.num_heads = num_heads
        self.attention_head_size = int(embed_dim / num_heads)
        self.all_head_size = self.num_heads * self.attention_head_size

        # Linear layers
        self.query = nn.Linear(embed_dim, embed_dim, bias=False)
        self.key = nn.Linear(embed_dim, embed_dim, bias=False)
        self.value = nn.Linear(embed_dim, embed_dim, bias=False)

        # Multi-Head Attention layers
        self.fc1 = nn.Linear(embed_dim, embed_dim)
        self.fc2 = nn.Linear(embed_dim * 2, embed_dim)

    def transpose_for_scores(self, x):
        new_x_shape = x.size()[:-1] + (self.num_heads, self.attention_head_size)
        x = x.view(*new_x_shape)
        return x.permute([0, 2, 1, 3])

    def forward(self, input_tensor):
        q = self.query(input_tensor)
        k = self.key(input_tensor)
        v = self.value(input_tensor)

        # This operation is independent of the size of batch size
        query_layer = self.transpose_for_scores(q)
        key_layer = self.transpose_for_scores(k)
        value_layer = self.transpose_for_scores(v)

        # scaled dot-product attention on query, key, and value tensors (B x N x M x K), where:
        # B is the batch size, N is the number of heads, M is the length of the sequence, and K is the dimension of each head.
        energy = torch.matmul(query_layer, key_layer.transpose(-2, -1))

        attention_weights = self._scaled_dot_product_attention(energy) # (B x N x 1 x M), where: (B, N, 1, M) is the batch size x the number of heads x length x dimensions per head
        context_layer = attention_weights.matmul(value_layer) # (B x N x 1 x K), where:
        # B is the batch size, N is the number of heads, and K is the dimension of each head.

        # concatenation to produce Bx(N*H)
        concatenated_context = self._concat_heads(context_layer)

        output = self.fc1(concatenated_context)
        output = self.fc2(output)
        
        return output

    def _scaled_dot_product_attention(self, attention_energy): # (B x N x 1 x M), where: 
        # B is the batch size, N is the number of heads, and K is the dimension of each head.
        attention_weights = torch.softmax(attention_energy, dim=-1)
        
        return attention_weights

    def _concat_heads(self, context_layer): # (B x N x 1 x M), where: 
        # B is the batch size, N is the number of heads, and K is the dimension of each head.
        new_context_layer_shape = context_layer.size()[:-2] + (self.all_head_size,)
        concatenated_context = context_layer.view(*new_context_layer_shape)

        return concatenated_context


# Initializing the model
m = MultiHeadAttention(embed_dim=64, num_heads=8)
