
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_encoder = torch.nn.Linear(64, 128) # Encoder to map queries and keys into a shared hidden space
        self.value_encoder = torch.nn.Linear(64, 256) # Encoder to map query and keys from the key embedding into values

    def forward(self, qk): # Function that computes attention scores between queries and keys in the batch
        v1 = self.key_encoder(qk[:,0]) 
        v2 = self.value_encoder(qk[:,1])

        v3  = torch.matmul(v1, v2)
        softmax_v3 = torch.softmax(v3, dim=-1) # Softmax is applied to the dot product of queries and keys
        
        dropout_v3 = torch.nn.functional.dropout(softmax_v3, p=0.5) # Dropout on attention scores

        v4 = torch.matmul(dropout_v3, v2)
        return v4


# Initializing the model
m  = AttentionModel()


# Inputs to the model
qk  = torch.randn(16, 2, 512) # [batch size * num heads * length of keys (seq_len)] and [batch size * num heads * length of queries (seq_len)]
