
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 30528)
        self.dropout1 = torch.nn.Dropout(p=dropout_p)
        self.dropout2 = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x):
        v = self.matmul(x)
        # [bs, seq_len, num_heads, head_size]
        k = v[:, :, :8].transpose(-2, -1)
        # [bs, seq_len, num_heads, seq_len]
        q = v[:, :, 8:].transpose(-2, -1)
        output = self.dropout1(torch.matmul(q, k))
        return self.dropout2(output).permute(0, 2, 3, 1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 48, 768)
