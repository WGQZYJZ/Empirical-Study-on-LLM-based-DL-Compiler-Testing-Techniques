
class Attention(torch.nn.Module):
    def __init__(self, q_dim: int, k_dim: int):
        super().__init__()
        self.q_fc = torch.nn.Linear(q_dim, num_heads * k_dim) # Project the query dimension to a multiple of head number (the output size in the paper is different from this)
        self.k_fc = torch.nn.Linear(k_dim, num_heads * k_dim) # Project the key dimension to a multiple of head number (the output size in the paper is different from this)
 
    def forward(self, q1: torch.Tensor, k1: torch.Tensor):
        # 1) Query transformation
        vq = self.q_fc(q1).reshape(-1, num_heads, -1)
 
        # 2) Key transformation
        vk = self.k_fc(k1).reshape(-1, num_heads, -1)
 
        # 3) Dot product between the query and key tensors (qk)
        # Use torch.matmul() to compute the dot product of vq and vk and put it in a matrix shape (-1, num_heads * k_dim)
        # For example: (8 x 128 x 576) x (8 x 1024 x 576) = (8 x 128 x 1024)
        qk = torch.matmul(vq, vk.transpose(-2, -1))
 
        # 4) Scale the dot product by a factor and then softmax-transform it (scaled_qk)
        scale_factor = torch.sqrt(torch.Tensor([q_dim])).to(device)
        scaled_qk = qk.mul(scale_factor).softmax(-1)
 
        # 5) Apply dropout and combine the query, key, and value in a matrix shape (-1, num_heads * k_dim) (dropout_qk)
        # Use torch.nn.functional.dropout() to apply dropout on scaled_qk
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=0.5)
 
        # 6) Compute the dot product of the query tensor and the value tensor to combine (output)
        # For example: (8 x 128 x 1024) x (8 x 128 x 1024) = (8 x 128 x 1024)
        output = torch.matmul(dropout_qk, vk).reshape(-1, num_heads * k_dim)
 
        return output
