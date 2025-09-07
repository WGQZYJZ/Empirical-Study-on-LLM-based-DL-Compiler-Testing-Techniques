
class MultiHeadAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.num_heads = config["num_heads"]  # Number of heads in the attention block
        self.dropout_p  = config["attention"]["dropout_rate"]  # Dropout rate for dropout in the attention block
        self.head_dim = config["d_model"] // self.num_heads # Calculate the head dimension
 
        self.query = nn.Linear(config["d_model"], self.head_dim)  # Linear projection of query weights
        self.key = nn.Linear(config["d_model"], self.head_dim)  # Linear projection of key weights
        self.value = nn.Linear(config["d_model"], config["d_model"])  # Project value weights
 
        self.attn_mask = get_causal_attention_mask(
            src_len=self.key.weight.shape[-2],
            max_len=self.query.weight.shape[-1]
        )
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):
        # Compute the dot product of the query and key, and scale it by a factor sqrt(head_dim)
        scaled = (self.query(query).transpose(-2, -1) @ self.key(key)) / math.sqrt(
            self.head_dim  # Calculate the scaling factor as square root of the head dimension
        )
 
        # Add the attention mask to the scaled dot product
        attn = scaled + self.attn_mask.to(scaled.dtype)
 
        # Apply softmax on the scaled dot product
        weights = F.softmax(attn, dim=-1)
        # Apply dropout and compute the dot product of the dropout output with the value weight tensor
        return torch.einsum("bnij->bni",  # Einstein notation for matrix multiplication
                            self.dropout_p > 0.,  # Check if there is a dropout rate larger than zero
                            weights @ self.value(key))
 
attn = MultiHeadAttention({
    "num_heads": num_heads,
    "d_model": d_model, 
    "attention":{"dropout_rate": 0}  # Set dropout to zero for this example
})

