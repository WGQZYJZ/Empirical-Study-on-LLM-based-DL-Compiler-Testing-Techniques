
class Model(torch.nn.Module):
    def __init__(self, q_dim, k_dim, v_dim):
        super().__init__()
        self.w_q = torch.nn.Linear(q_dim, dim, bias=False)
        self.w_k = torch.nn.Linear(k_dim, dim, bias=False)
        self.w_v = torch.nn.Linear(v_dim, dim, bias=False)
 
    def forward(self, q1, k1, v1):
        # Compute the dot product of the query and key
        dk  = -2 * math.log(query.size(-2))  # Precompute the dimension to reduce computation later
        wq  = self.w_q(q1).unsqueeze(dim=-2)  # Apply a linear transformation to the query
        wk  = self.w_k(k1).unsqueeze(dim=1)  # Apply a linear transformation to the key
        vv  = self.w_v(v1).unsqueeze(dim=0)  # Apply a linear transformation to the value
        wq  = torch.matmul(wq, wk) + dk 
        attn_weights  = torch.softmax(wq, dim=-1)  # Compute attention weights with softmax
        attn_weights  = torch.dropout(attn_weights, dropout_p, True)  # Dropout the attention weights

        return output

# Initializing the model
m = Model()


def query(x1):
    q1 = m.w_q(x1).unsqueeze(dim=-2)
    k1 = m.w_k(x1).unsqueeze(dim=1)  # x = [bs, c]
    v1 = m.w_v(x1).unsqueeze(dim=0)

def 