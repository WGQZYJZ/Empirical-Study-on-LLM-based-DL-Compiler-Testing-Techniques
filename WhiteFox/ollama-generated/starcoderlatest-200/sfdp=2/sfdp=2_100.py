
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, num_heads=8, dropout_p=0.1):
        super().__init__()
        self.num_heads = num_heads
        # Linear transformation layer for computing queries and keys of multi-head attention
        self.query_layer = torch.nn.Linear(512, 64)
        # Linear transformation layer for computing values of multi-head attention
        self.key_value_layer = torch.nn.Linear(512, 512 * 3)
 
        # Multi-head attention module with scaled dot product and softmax applied after concatenation to the output of the linear layer for computing values of multi-head attention
        self.multi_head_attention = torch.nn.MultiheadAttention(num_heads=self.num_heads,
                                                                    input_dim=64,
                                                                    dropout=0)
 
    def forward(self, x1):
        # Generate queries (t1) and keys (v2) with size 512 for the query layer
        t1 = self.query_layer(x1).permute(0, 2, 3, 1)
        v2 = self.key_value_layer(x1).permute(0, 2, 3, 4, 1)
        # Perform multi-head attention
        