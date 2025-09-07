
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(16, 32)
        self.value = torch.nn.Linear(32, 32)
        self.dropout_p = torch.nn.Dropout(p=0.5)

    def forward(self, qk, attn_mask):
        v2 = self.key(qk)
        output = self.dropout_p(attn_weight * v2) @ self.value

# Initializing the model
m = Model()


# Inputs to the model
qk = torch.randn(1, 32, 8, 64) # query and key tensor
attn_mask = torch.ones(8, 64, dtype=torch.float) # attention mask (if needed)
