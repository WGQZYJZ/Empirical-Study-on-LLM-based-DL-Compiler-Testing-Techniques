
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 3052)
        self.attn = ScaledDotProductAttention()
 
    def forward(self, x):
        x = self.linear1(x)
        return self.attn(q=x).squeeze(-1)
 
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q):
        # This function computes the attention weights: Attention_weights = softmax(q@k/(d_k^0.5))
        return torch.matmul(q, k).softmax()
 
class MultiHeadAttention(torch.nn.Module):
    