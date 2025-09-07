
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(1024, 512)
 
    def forward(self, qk_v_t):
        # Get the query, key, value and temporal tensor from the input
        qk, v, t = qk_v_t[:, :3], qk_v_t[:, 3:6], qk_v_t[:, -1]
        # Compute the dot product of the query and key tensors and softmax it
        scaled_qk = torch.matmul(qkv[0], qkv[1].transpose(-2, -1))
        v = self.attn(t) + self.attn(v)  # Add the attention output from time t to the value tensor
        return v


# Initializing the model
m = Model()

# Inputs to the model
qkv_t  = torch.randn(2, 1024, 65, dtype=torch.float32)
qk_v_t = qkv_t[:, :3], qkv_t[:, 3:6], qkv_t[:, -1]
