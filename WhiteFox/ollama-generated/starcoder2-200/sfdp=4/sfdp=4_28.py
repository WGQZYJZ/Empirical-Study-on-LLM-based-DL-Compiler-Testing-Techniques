
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):

        k  = torch.matmul(input1, input2) / math.sqrt(input1.size(-1))
        k  = k + attn_mask
 
        v  = input1 @ input2.transpose(-2, -1) * math.sqrt(input1.size(-1))
        v  = k + attn_mask
        v  = torch.softmax(v, dim=-1)

        return v

m  = Model()

