
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(4096, 20)
 
    def forward(self, x1, x2):
        # Query-key pair to compute the attention weights
        kq = (x1 @ x2.transpose(-2, -1)) / math.sqrt((x1.size(-1)))
        kq += torch.FloatTensor([[[0] * 8], [[0] * 4], [[0] * 4], [[0] * 4]])
        # Attention weights are computed as the softmax of the scaled dot product of the query and key tensors
        attn_weight = torch.softmax(kq, dim=-1)
        # Output is computed as the weighted sum of the value tensor (the second part of the dot-product)
        output  = attn_weight @ x2.transpose(-2, -1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(8, 20, 128, 128)
