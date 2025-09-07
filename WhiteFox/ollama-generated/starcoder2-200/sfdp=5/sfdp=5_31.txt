
class MultiheadAttention(torch.nn.Module):
    def __init__(self, n_heads: int = 8):
        super().__init__()
 
        self.n_heads = n_heads
 
        self.query_dense = torch.nn.Linear(768, 768)
        self.key_dense   = torch.nn.Linear(768, 768)
        self.value_dense = torch.nn.Linear(768, 768)
 
    def forward(self, query: torch.Tensor):
        query_inputs = self._reshape(query)
 
        query1, key1, value1 = self.attn_forward(
            query1=query_inputs[0],
            key2=query_inputs[1],
            value3=query_inputs[2]
        )
 
        query2 = self._split(query1).transpose(-2, -1) @ self._split(key1).transpose(-2, -1) / math.sqrt(768)
        query2  = self._softmax(query2 + query_inputs[3])
        query3  = torch.dropout(query2, 0.1, True)
 
        output = self._split(value1).transpose(-2, -1) @ self._split(query3).transpose(-2, -1)
        return output
 
    def attn_forward(self):
        # Compute attention weights.
        key   = self.key_dense(self.query)
        value = self.value_dense(self.query)
 
        self.attn  = (key @ value.transpose(-2, -1)) / math.sqrt(768)
 
        self.attn += self._create_attn_mask()
 
        self.attn   = torch.softmax(self.attn, dim=-1)
        self.attn   = torch.dropout(self.attn, 0.1, True)
 
        self._query3  = value @ self.attn
        return query1, key1, value1


# Initializing the model
attn_m = MultiheadAttention()
attn_m2 = copy.deepcopy(attn_m)

# Inputs to the model
input1  = torch.randn(64,  8 * 3072) # The input to the query layer
input2  = torch.randn(64,   3072) # The input to the key layer
input3  = torch.randn(64,    768) # The input to the value layer
input4  = torch.randn(129)         # Attention mask

__output_m1__  = attn_m(input1)   # Forward pass on the first time without dropout and without attention mask
__output_m2__  = attn_m2(input1)  # Forward pass with dropout


# Inputs to the model