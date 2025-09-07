
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, q, k, v):
        # The query, key, and value tensors must be in the same number of dimensions. For example, if they were images or videos, then their dimensions would have the shape [B, C, T].
        query = torch.nn.functional.interpolate(q, size=v.shape[-2:])  # Interpolate to match v's height and width
        