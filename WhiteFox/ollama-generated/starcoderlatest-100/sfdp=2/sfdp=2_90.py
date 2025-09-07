
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, x1, x2, query, key, value):
        qk = self.attention(x1, x2, x3)
        softmax_qk = self.attention(x1, x2, x3)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)


# Input to the model
input1  = torch.randn(8, 5, 64, 64) # (B, H, W, C) - Batch size: 32, Hidden dim: 128, Width and height of the image: 32, number of channels for the image
input2 = torch.randn(8, 8, 128, 64) # (B, H, W, C) - Batch size: 32, Hidden dim: 128, Width and height of the image: 32, number of channels for the image
query = torch.randn(16, 128, 8, 64) # (B, N_head, T_q, H, W, C) - Batch size: 32, Hidden dim: 128, Width and height of the image: 32, number of channels for the image
key = torch.randn(16, 5, 128, 64) # (B, N_head, T_k, H, W, C) - Batch size: 32, Hidden dim: 128, Width and height of the image: 32, number of channels for the image
value = torch.randn(16, 5, 128, 64) # (B, N_head, T_v, H, W, C) - Batch size: 32, Hidden dim: 128, Width and height of the image: 32, number of channels for the image
