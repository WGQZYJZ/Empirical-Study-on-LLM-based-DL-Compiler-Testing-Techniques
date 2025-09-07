
class SelfAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
        self.fc_q = torch.nn.Linear(dim, dim)  # Compute query weights
        self.fc_k = torch.nn.Linear(dim, dim)  # Compute key weights
        self.fc_v = torch.nn.Linear(dim, dim)  # Compute value weights
 
        self.attn_mask = torch.nn.Parameter(torch.ones(1))
 
    def forward(self, query, key, value):
        qk = self._scaled_dot_product(query, key)  # Dot product between the query and key
        attn_weights = F.softmax(qk + self.attn_mask, dim=-1)  # Compute attention weights using softmax and masking for padding tokens
        output = torch.matmul(attn_weights, value)  # Perform matrix multiplication to obtain weighted sum of values
        return output
 
    def _scaled_dot_product(self, query, key):
        qk = (query @ self.fc_q(query).transpose(-2, -1)) + (key @ self.fc_k(key).transpose(-2, -1))  # Compute scaled dot product between the query and key
        return qk
 
 class MultiHeadAttention(torch.nn.Module):
     def __init__(self, dim, num_heads=4):
         super().__init__()
 
         self.num_heads = num_heads
         self.dim = dim
 
         assert dim % num_heads == 0
         self.dim_per_head = dim // num_heads
 
  def forward(self, query, key, value, mask=None):
      # Convert all of the inputs to flat Tensors before flattening:
      q = self._flatten_tensor(query)
      k = self._flatten_tensor(key)
      v = self._flatten_tensor(value)
 
      # Linear layer normalization for query, key, and value:
      q = torch.nn.LayerNorm(q)
      k = torch.nn.LayerNorm(k)
      v = torch.nn.LayerNorm(v)
 
      # Transpose dimensions of q, k, and v to move the batch dimension to be the first dimension:
      query = self._transpose_for_matmul(q)  # [batch, head, seq_len, dim]
      key = self._transpose_for_matmul(k)  # [batch, head, seq_len, dim]
      value = self._transpose_for_matmul(v)  # [batch, head, seq_len, dim]
 
      # Split heads:
      query = self._split_heads(query)  # [batch, head, seq_len, dim]
      key = self._split_heads(key)  # [batch, head, seq_len, dim]
      value = self._split_heads(value)  # [batch, head, seq_len, dim]
 
      # Multiply-add dot products:
      attention_scores = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Dot product between the query and key
      if mask is not None:
          assert mask.dim() == 4
          assert mask.size(-2) == query.size(-2)
          assert mask.size(-1) == key.size(-1)
 
          attention_scores = attention_scores + (mask * -1e9)
 
      attention_weights = F.softmax(attention_scores, dim=-1)  # Softmax to obtain the soft attention weights for each head at each position
      attention_output = torch.matmul(attention_weights, value)  # Dot product between attention weights and value; this is now a weighted sum of values
 
      # Combine heads back into original dimension:
      attention_output = self._transpose_to_original_dim(attention_output)  # [batch, seq_len, dim]
      attention_output = self._merge_heads(attention_output)  # [batch, head * dim, seq_len]
 
      return attention_output
 
  def _split_heads(self, x):
      batch, seq_len, dim = x.size()
 
      assert (
          self.dim % self.num_heads == 0
      ), "Cannot split tensor into {} heads because total dimension is not a multiple of the number of heads".format(
          self.num_heads)
 
      # Squeeze last dimension to make sure it's the same size as dim:
      x = x.contiguous().view(batch, seq_len, -1)  # [batch, seq_len, num_heads * dim]
 
      # Transpose dimensions of x to make them a tensor with shape (batch, num_heads, seq_len, dim)
      return x.transpose(0, 1).contiguous().view(batch, self.num_heads, -1, dim)  # [batch, num_heads, head_dim, seq_len]
 
  def _merge_heads(self, x):
      batch, num_heads, _, dim = x.size()
 
      return x.transpose(0, 1).contiguous().view(batch, -1, dim)  # [batch, seq_len, dim]
 
  def _flatten_tensor(self, x):
      x = x.contiguous().view(-1, self.dim)  # [batch * seq_len, dim]
      return x
 
  def _transpose_for_matmul(self, x):
      batch, head, seq_len, dim = x.size()
 
      return x.permute(0, if (self._, \ _ in the first paragraph).
  - [The Beast that Could Could Could](https://www.youtube.com/embed/D784x3s0dUQ)
