
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 16)
        self.key   = torch.nn.Linear(16, 48)
        self.value = torch.nn.Linear(48, 2)
 
    def forward(self, x1):
        # Get the last dimension of both query and key tensors
        n = x1.shape[-1]
        # Apply a dot product with query and key, which reduces to n * n matrix
        v_q_k   = torch.matmul(x1, self.key) / math.sqrt(self.query.weight.shape[0])  # (B, K, D)
        # Compute the softmax weights, which is just a normalized version of v_q_k
        attn_weights = torch.nn.functional.softmax(v_q_k, dim=-1)  # (B, K, K)
        # Compute the value vector
        self_attention_output = torch.matmul(attn_weights, self.value)  # (B, K, D)
        return self_attention_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
