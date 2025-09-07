
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # query_key: [batch_size, query_length, key_length]
        query_key = self.conv(x1).view(-1, x1.size(2), x1.size(3))  # [batch_size * query_length * key_length]
        # attn_mask: [batch_size, query_length, key_length]
        attn_mask = torch.zeros(query_key.shape[0], query_key.shape[1], query_key.shape[2])  # [batch_size, query_length, key_length]
        for i in range(attn_mask.shape[1]):
            for j in range(attn_mask.shape[2]):
                attn_mask[range(query_key.shape[0]), i, j] = (torch.arange(
                    start=i,  end=query_key.shape[1], step=1), torch.arange(
                    start=j,  end=query_key.shape[2], step=1)).view(-1, 1)
        attn_mask = attn_mask / math.sqrt(query_key.size(-1))
        # attn_weight: [batch_size * query_length, key_length]
        attn_weight = torch.softmax(query_key @ query_key, dim=-1)  # [batch_size * query_length, key_length]
        output = attn_weight @ x1  # [batch_size * query_length, value_length]
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
