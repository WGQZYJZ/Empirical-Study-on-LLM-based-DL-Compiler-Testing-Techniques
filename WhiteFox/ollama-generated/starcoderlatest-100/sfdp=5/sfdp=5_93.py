
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(1024, 8)
        self.attn_k = torch.nn.Linear(1024, 8)
        self.attn_v = torch.nn.Linear(1024, 8)
 
    def forward(self, q1):
        v1 = self.attn_q(x1) @ self.attn_k.transpose(-2, -1) / math.sqrt(1024) + attn_mask
        v2 = torch.softmax(v1, dim=-1) 
        v3 = torch.dropout(v2, dropout_p, True) * 0.5
        output = (attn_weight @ value).matmul(k3) # Apply a matrix multiplication between the attention weight and the key value for each head, then sum over the heads

        return output


# Initializing the model
m = Model()

x1 = torch.randn(20, 16, 128, 128)
attn_mask = torch.zeros([1, x1.shape[0], x1.shape[1], x1.shape[2]], dtype=torch.float32).cuda()
v4 = torch.softmax(v1, dim=-1)
v5 = torch.dropout(v2, dropout_p, True) * 0.7071067811865476 # 4x more computation compared to the previous example
attn_weight = (attn_mask @ k3).softmax(dim=-1)

