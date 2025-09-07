
class Model(torch.nn.Module):
    def __init__(self, nhead=1024, query  = None):
        super().__init__()
        self.scalefactor = torch.tensor([6])
        self.attn1 = torch.nn.MultiheadAttention(
            embed_dim=nhead * 3, num_heads=nhead)
 
    def forward(self, query, key):
        scaled_qk  = torch.div(torch.matmul(query, key.transpose(-2, -1)), self.scalefactor) 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        return dropout_qk.matmul(torch.randn([32], [64]))


# Initializing the model
m = Model()
m(torch.randn([1]), torch.randn([1]))
# Inputs to the model
x1 = torch.tensor([[0.5975, -0.8545]])
x2 = torch.tensor([[ 0.3496],
        [-0.6292],
       [ 0.7531],
       ...,
          [ 1.],
          ...]])

