
class AttentionLayer(torch.nn.Module):
    def __init__(self,
                 k: int = 128,
                 v: int = 64):
        super().__init__()

        self._k = k # Dimensionality of queries in MultiHeadSelfAttentionLayer
        self._v = v # Dimensionality of keys and values in MultiHeadSelfAttentionLayer

    def forward(self,
                query: torch.Tensor,
                key: torch.Tensor,
                attn_mask: torch.Tensor) -> (torch.Tensor, torch.Tensor):

        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)

        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return query * attn_weight[:, None] + output, qk


class MultiHeadSelfAttentionLayer(torch.nn.Module):
    def __init__(self,
                 input_dim: int = 64,
                 num_heads: int = 2,
                 dropout_p: float = 0.1):
        super().__init__()

        self._num_heads = num_heads # Number of attention heads
        self._input_dim = input_dim # Dimensionality of model inputs
        
        # We initialize our query and key weights with normal distribution
        torch.nn.init.normal_(self.query, std=0.01)
        torch.nn.init.normal_(self.key, std=0.01)

        self._dropout = nn.Dropout(p=dropout_p) # Create a dropout operation instance
        
        # Create the parameters for all of the attention heads in our model.
        self.attentions: List[nn.Module] = [AttentionLayer() for _ in range(num_heads)]
        
        # This line computes the dimensionality of the linear projections that we apply to the query, key, and value from each head
        self._scaled_query: int = input_dim * num_heads

        torch.nn.init.normal_(self.value, std=0.01)

    def forward(self,
                query: torch.Tensor,
                key: torch.Tensor,
                attn_mask: torch.Tensor,
                return_attn_weights: bool = True) -> (torch.Tensor, torch.Tensor):
        # Shape of query and key should match the model input shape except for the last dimension
        _batch_size, q_dim = query.shape[:2]
        _num_heads, k_dim = key.shape[:2]

        # First we compute a scaled dot product between the query and key for each head, so that each attention head has access to different aspects of the data:
        qk = torch.matmul(query.reshape(-1, q_dim).unsqueeze(-1), self.query.transpose(0, -2)).reshape(_batch_size, _num_heads, -1)
        kq = torch.matmul(key.reshape(-1, k_dim).unsqueeze(1), self.key.transpose(0, 1)).reshape(_batch_size, _num_heads, -1)

        # Next we apply a dropout operation so as to prevent the model from overfitting during training.
        qk = self._dropout(qk)

        # Now that each head has access to different aspects of the input data, we can compute the attention weights:
        for i, attn in enumerate(self.attentions):
            attn_output, _ = attn(qk, kq, attn_mask)
            
            # Concatenate heads of output from each attention layer into a single tensor so that the model has access to all heads of information
            qk = torch.cat((qk, attn_output), dim=-2)

        # Now we need to reshape the result of this process so as to have the same number of dimensions and dimensions in each head
        qk = qk.reshape(_batch_size, _num_heads * k_dim, -1).permute(0, 2, 1).contiguous()
        
        value = torch.matmul(qk, self.value)

        if return_attn_weights:
            attn_weights = qk @ torch.transpose(self.key, -2, -1)
            attn_weights = attn_weights / math.sqrt(q_dim)

            # The first dim is the batch size and the second one is the attention weights for each head (one entry per key in each query). The last dimension is equal to k_dim * input_dim because the qk variable has been reshaped as above
            attn_weights = torch.transpose(attn_weights, 0, 1)

            return value, qk, attn_weights

        return value, qk

class MultiHeadAttentionNetwork(torch.nn.Module):
    def __init__(self,
                 input_dim: int = 3,
                 num_heads: int = 2,
                 dropout_p: float = 0.1):
        super().__init__()
        
        # Create the multi-head self-attention layer instance that we will use to compute attention weights between query and key in each head of this network.
        self._multi_head_attn = MultiHeadSelfAttentionLayer(
            input_dim=input_dim, 
            num_heads=num_heads, 
            dropout_p=dropout_p)

    def forward(self,
                if isinstance None = 0 = 1.0
} // end of namespace Gadgetron

