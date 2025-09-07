
class Model(torch.nn.Module):
    def __init__(self, dim_head=None):
        super().__init__()
        self.dim_head = dim_head
        if dim_head == None:
            # Use a default value to match the reference model in Appendix C of the paper
            self.num_heads = 16
            self.dim_head = 32
        else:
            self.num_heads = dim_head
            self.dim_head = dim_head * 4

        self.conv_q = torch.nn.Conv2d(3, self.num_heads, 3, stride=1)
        self.conv_k = torch.nn.Conv2d(3, self.num_heads, 3, stride=1)
        self.conv_v = torch.nn.Conv2d(3, self.num_heads, 3, stride=1)

        self.linear_q = torch.nn.Linear(self.num_heads * self.dim_head, 8 * self.num_heads) # [batch_size x n_samples x seq_length]
        self.linear_k = torch.nn.Linear(self.num_heads * self.dim_head, 8 * self.num_heads) # [batch_size x n_samples x seq_length]
        self.linear_v = torch.nn.Linear(self.num_heads * self.dim_head, 8 * self.num_heads) # [batch_size x n_samples x seq_length]

        self.attn = torch.nn.MultiheadAttention(embed_dim=8*self.num_heads, num_heads=16, dropout=dropout_p, batch_first=True)

    def forward(self, x1):
        v1 = self.conv_q(x1).permute(0, 3, 2, 1) # [batch_size x n_samples x seq_length]
        v2 = self.conv_k(x1).permute(0, 3, 2, 1) # [batch_size x n_samples x seq_length]
        v3 = self.conv_v(x1).permute(0, 3, 2, 1) # [batch_size x n_samples x seq_length]

        v4 = torch.cat((v1, v2, v3), dim=1)
        v5 = self.linear_q(v4).view(-1, self.num_heads, 8*self.dim_head) # [batch_size x n_samples x seq_length]
        v6 = self.linear_k(v2).view(-1, self.num_heads, 8*self.dim_head) # [batch_size x n_samples x seq_length]
        v7 = self.linear_v(v3).view(-1, self.num_heads, 8*self.dim_head) # [batch_size x n_samples x seq_length]

        v8, _ = self.attn(v5, v6, v7, need_weights=False) # [batch_size x seq_length x num_heads x dim_head]
        output = torch.nn.functional.dropout(torch.nn.functional.relu(v8), p=dropout_p).view(-1, 32 * self.num_heads, 64, 64) # [batch_size x seq_length x num_heads*dim_head]
        return output


# Initializing the model
m = Model(16)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
