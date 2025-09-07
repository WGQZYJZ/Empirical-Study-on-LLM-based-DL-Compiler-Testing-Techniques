
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, h: int = 8, d_model=512) -> None:
        super().__init__()
 
        self.d_k  = 64 # The size of the key is set to 64.
        self.h  = h # The number of heads for this model is 8.
        self.head_dim  = d_model // self.h
 
         self.dropout  = torch.nn.Dropout(0.1)
 
        # Initialize a parameter called query_layer, which consists of three sublayers:
        # Linear layer (linear_layer), batch normalization layer (attn_norm), and dropout layer (dropout).
        # Parameters are named query_layers, attn_norms, and dropouts respectively.
        self.query_layers  = torch.nn.ModuleList(
            [
                torch.nn.Sequential(
                    torch.nn.Linear(d_model, d_model),
                    torch.nn.LayerNorm(d_model),
                    torch.nn.Dropout(0.1),
                ) for _ in range(3) # The number of sublayers is 3.
            ]
        )
 
        self.attn = ScaledDotProductAttention()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask=None):
         batch_size  = query.shape[0]
 
         # Convert the query to multiple heads by applying the dot product of the keys with the query, and then normalizing it.
         query  = self.attn(query)
 
 
        # Compute the dot product of the query and key, normalize it, apply dropout on it, multiply them by the value, and then concatenate these three results.
        output1, output2  = self.mlp_layers(query), self.multihead_attn()
        return output3


# Initializing the model
m = MultiHeadedAttention()
 
 # Inputs to the model
  key = torch.randn([batch_size] * 4)
   value = torch.randn([batch_size, 8] * 4)
    attn_mask1 = torch.randn([32])
       attn_mask2 = torch.zeros(6)
        attn_mask3 = torch.randn([50], dtype=torch.bool)
 
# Outputs of the model
__output__  = m(key, key, value, mask=[attn_mask1] * 4 + [attn_mask2]) # The shape is (batchsize x 8 x dmodel).
 
