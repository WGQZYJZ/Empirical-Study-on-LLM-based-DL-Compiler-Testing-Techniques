
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_fc1 = torch.nn.Linear(512, 64)
        self.attn_fc2 = torch.nn.Linear(64, 32)

    def forward(self, q1, k1, v1, attn_mask):
        a1 = F.tanh(self.attn_fc1(torch.cat((q1, k1), dim=-1)))
        s1 = torch.matmul(a1, self.attn_fc2(v1))
        w1  = torch.softmax(s1, dim=-1) # Apply softmax to the result
        v2 = torch.matmul(w1, v1) # Compute the dot product of the attention weights and the value tensor
        return v2


# Initializing the model
m = Model()
q1 = torch.randn(4, 3, 512)
k1 = torch.randn(8, 3, 512)
v1 = torch.randn(8, 3, 512)
attn_mask = torch.Tensor([ [ [True, True, False, False],
                               [False, False, True, True] ],
                              [ [False, False, False, False],
                               [True, True, True, True] ] ])


# Inputs to the model
