
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 32)
        self.attn_mask = torch.zeros((1, 3, 64, 64), device='cuda:0', dtype=torch.float32)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x1):
        qkv = self.qkv(x1).chunk(3, dim=-1)  # Split the input by batch, channel and feature dimensions respectively
        attn_mask = self.attn_mask.unsqueeze(0)

        # Get attention weights from scaled dot product of query with key
        attn_weight = self.softmax(qkv @ qkv.transpose(-2, -1))  # Softmax the result by using the attn_mask
        attn_weight = torch.dropout(attn_weight, dropout_p, True)

        # Get output from scaled dot product of attention weights with value
        output = attn_weight @ x1  # The result is also a dot product between the query and key, so just get it back
        return output


# Initializing the model
m = Model()


