
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.value_conv = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        # q and k are the two linear submodules that compute the dot product of the query and key
        q  = self.attn_conv(x1)  # x1 @ x1.transpose(-2, -1) = x1 @ x1^T + a_i
        k  = self.attn_conv(x2)  # x2 @ x2.transpose(-2, -1) = x2 @ x2^T + a_i

        # dropout on attention weights and value
        attn_weight = torch.softmax(q @ k / math.sqrt(q.size(-1)), dim=-1)  # [16 x 8] x [16 x 3] -> [16 x 8 x 3]
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = q @ attn_weight @ self.value_conv(output)

# Initializing the model
m = Model()

