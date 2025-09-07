
class Model(torch.nn.Module):
    def __init__(self, d_model=512, num_heads=8, depth=6, max_len=1024, head_size=32):
        super().__init__()
        self.query = torch.nn.Linear(d_model, head_size)
        self.key   = torch.nn.Linear(d_model, head_size)
        self.value = torch.nn.Linear(d_model, head_size)
 
        num_heads = 12
        d_head    = head_size // num_heads
 
        for i in range(depth):
            self.__setattr__('attn_%d' % (i + 1),
                             torch.nn.MultiheadAttention(head_count=num_heads,
                                                             key_dim   = d_model,
                                                             dropout    = False))

        # Feed the output of MultiheadAttention to a dense layer
        self.out = torch.nn.Linear(d_model * (depth + 1), d_model)
 
    def forward(self, x):
        # qk: 2048x2048
        q = self.query(x).permute(1, 0, 2).contiguous()
        k = self.key(x).permute(1, 0, 2).contiguous()
        v = self.value(x)
 
        # At the first layer, we will only compute attention from the query to its own key and the value.
        attn_output = torch.cat([self.attn_1(q, k),
                                  self.attn_1(q, v)],
                                 dim=-1)

        # For other layers (other than the last one)
        for i in range(2, 3 + self.depth):
            qk = q @ k.transpose(-2, -1).contiguous() / math.sqrt(q.size(-1))
            qk += attn_mask

            attn_output = torch.cat([self.__getattr__('attn_%d' % (i)).forward(qk),
                                      attn_output],
                                     dim=-1)
 
        output = self.out(attn_output).permute(1, 0, 2)

        return output


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(8, 3, 64, 64)
