
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk  = torch.bmm(query, torch.transpose(key, -2, -1)) / math.sqrt(torch.size(-2, 0))
        qk += torch.Tensor([[-30.,  5., 3.], [-46.,-89,-70]])
        attn_weight = torch.softmax(qk, dim=-1) 
        output = attn_weight @ value # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m  = Model()


