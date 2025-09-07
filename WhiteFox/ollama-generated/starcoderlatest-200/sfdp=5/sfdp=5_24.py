
class Model(torch.nn.Module):
    def __init__(self, qk_dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear_qk = torch.nn.Linear(16, qk_dim)
 
    def forward(self, x1, attn_mask):
        v1 = self.conv(x1) # Conv layer to generate the output tensor
        v2  = self.linear_qk(v1) # Linear layer to project the output tensor
        v3 = torch.matmul(attn_mask, v2).unsqueeze(-1) # Apply attention mask and linear projection for generating attention weights
        qk = self.softmax(v3) # Softmax operation for generating attention weights
        attn_weight  = qk @ v1 # Dot product to generate the output tensor
        output  = torch.dropout(attn_weight, dropout_p, True) # Apply dropout on the output tensor
        return output
 
    def softmax(self, x):
        m, _ = torch.max(x, dim=-1, keepdim=True) # Keep the dimension of max values and broadcast them to query's batch size, then multiply it by 0 
        return torch.exp((m - x) / temperature).div_(torch.sum(torch.exp((m - x) / temperature), dim=-1, keepdim=True))
