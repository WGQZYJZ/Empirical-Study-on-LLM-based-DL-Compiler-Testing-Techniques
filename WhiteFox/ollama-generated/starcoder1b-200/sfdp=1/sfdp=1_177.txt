
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(d_model, d_k)
        self.k = torch.nn.Linear(d_model, d_k)
        self.v = torch.nn.Linear(d_model, d_v)
        self.o = torch.nn.Linear(d_k + d_v, n_head * h)
        self.attn = torch.nn.Softmax()
 
    def forward(self, x1, x2):
        k1, k2  = self.q(x1), self.k(x2)
        v1, v2  = self.v(x1), self.v(x2)
        attn_mask = torch.pow(torch.sum((self.attn(k1, k2) + EPSILON), dim=-1).unsqueeze(-1), 0.5)  # Compute the attention mask used for computing the weighted dot product
        x3 = torch.matmul(attn_mask, (v1.transpose(-2, -1) * v2))  # Weighted dot product between the value and the value of the scaled dot product of the query and the key tensor
        o = self.o(x3).view(bsz, n_head, h, d_k + d_v)  # Unpack the output
        return o


# Initializing the model
m = Model()


