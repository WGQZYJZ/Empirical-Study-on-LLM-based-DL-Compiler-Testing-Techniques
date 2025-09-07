
class Model(torch.nn.Module):
    def __init__(self, dim_q=16, dim_v=64):
        super().__init__()
        self.attn_weight = torch.nn.Linear(dim_q, dim_q)
        self.matmul_attn = torch.nn.Linear(dim_q, dim_q)
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, x):
        qk = self.matmul_attn(x)  # Perform a matmul between query and key, using the attention mask as well
        attn_weight = self.softmax(qk)  # Softmax on the scaled dot product of query and key
        output = torch.matmul(attn_weight, x)  # Multiply softmax result with the value
        return output
