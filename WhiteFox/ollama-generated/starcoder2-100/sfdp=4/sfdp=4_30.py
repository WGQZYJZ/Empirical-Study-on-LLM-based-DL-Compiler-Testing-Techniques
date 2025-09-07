
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value2, attn_mask):  # query: [b*196*d], key: [b*50*d] or [1*50*d], value: [batch*64*d], attn_mask: [k_len, batch * kdim]
        v1 = torch.matmul(query1 @ key1.transpose(-2, -1), math.sqrt(key1.size(-1)))  # query: [b*kdim], key: [b*kdim*vdim], value: [batch*kdim*vdim], attn_mask: [k_len, batch * kdim]
        v2 = v1 + attn_mask
        v3 = torch.softmax(v2, dim=-1)  # [batch*kdim, 50, kdim]
        output = torch.bmm(v3, value2).transpose(-2, -1)  # [batch * kdim , 50, vdim]
        return output

# Initializing the model
attn_model = AttentionModel()

# Inputs to the model
key1  = torch.randn(8*64, 196)  # batch size 256, sequence length 32, key dimension 64 (number of words in vocabulary)
query1 = key1[:, :, None] + torch.randn(8*64, 196).unsqueeze(-1)
value2 = value * 0.7071067811865476 # batch size 32, sequence length 50, value dimension 1 (number of labels)
attn_mask = torch.ones(50, 8*64)  # batch size 32, sequence length 50

